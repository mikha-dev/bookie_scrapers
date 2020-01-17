import logging

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from scrapers.base.odds_scraper import OddsScraper


class OddsPortal(OddsScraper):

    def __init__(self, url: str, data_path, competition_name):
        super().__init__(url, data_path, competition_name)

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
        try:
            finished = self.driver.find_element_by_xpath("//div[@id='event-status']").text

            if len(finished.strip()) > 0:
                return False

            odds = self.driver.find_elements_by_xpath("//tr[contains(@class, 'lo')]")
            odds = [list(map(lambda s: s.strip(), o.text.split("\n"))) for o in odds]
            odds = [o for o in odds if len(o) == 5]
            return odds

        except NoSuchElementException as _:
            pass
        except StaleElementReferenceException as _:
            pass

    def save(self, url, odds):
        print(url, odds)
