import itertools
from contextlib import suppress

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

from scrapers.base.odds_scraper import OddsScraper


class OddsPortal(OddsScraper):

    def __init__(self, url: str, repository_callback):
        assert url, "Must have a url"
        assert repository_callback, "Must supply a callback to process odds"

        super().__init__(url, repository_callback)

    def find_urls(self):
        """
        Finds all non active urls for a specific league.
        """

        urls = self.driver.find_elements_by_xpath(
            "//tr[not(contains(@class, 'deactivate'))]/td[@class='name table-participant']/a"
        )

        urls = list(filter(lambda url: url.get_attribute("href").startswith("https"), urls))

        urls = [url.get_attribute("href") for url in urls]

        return urls

    def find_and_parse_odds(self):
        with suppress(NoSuchElementException, StaleElementReferenceException):
            finished = self.driver.find_element_by_xpath("//div[@id='event-status']").text

            if len(finished.strip()):
                return "DONE!"

            odds = self.driver.find_elements_by_xpath("//tr[contains(@class, 'lo')]")
            odds = [list(map(lambda s: s.strip(), itertools.chain([self.driver.current_url], o.text.split("\n")))) for o
                    in odds]

            fields = ["url", "bookie", "1", "X", "2", "payout"]

            odds = [dict(zip(fields, o)) for o in odds if len(o) == 6]

            return odds
