import logging
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
            window_handles = self.driver.window_handles.copy()

            for window_handler in window_handles[1:]:

                self.driver.switch_to.window(window_handler)

                logging.info(f"parsing url: {self.driver.current_url:>5}")

                odds = parse_odds(self.driver)

                if odds == "FINISHED":
                    logging.info(f"closing game: {self.driver.current_url:>5}")
                    self.window_handler.close_tab()
                    continue

                self.odds_cache.add_new_odds(self.driver.current_url, odds)

                time.sleep(1)
