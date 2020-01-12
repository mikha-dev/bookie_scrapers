import time

from oddsportal.helpers.oddsportal import find_urls, parse_odds
from oddsportal.odds_cache import OddsCache
from oddsportal.scraper.base import BaseScraper


class OddsScraper(BaseScraper):
    def __init__(self, url: str, odds_cache: OddsCache):
        super().__init__(url)
        self.odds_cache = odds_cache

    def start(self):

        self.window_handler.open_page(self.url)

        urls = find_urls(self.driver)

        self.window_handler.open_tabs(urls)

        while True:

            for window_handler in self.driver.window_handles[1:]:
                self.driver.switch_to.window(window_handler)

                odds = parse_odds(self.driver)

                if odds == "FINISHED":
                    self.window_handler.close_tab()
                    continue

                self.odds_cache.add_new_odds(self.driver.current_url, odds)

                time.sleep(1)
