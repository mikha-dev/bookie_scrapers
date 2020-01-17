import logging
import time
from abc import abstractmethod

from scrapers.base.base import BaseScraper
from scrapers.base.odds_cache import OddsCache


class OddsScraper(BaseScraper):

    def __init__(self, url: str, data_path, competition_name):
        super().__init__(url)
        self.odds_cache: OddsCache = OddsCache(data_path, competition_name)

    @abstractmethod
    def find_urls(self):
        raise NotImplementedError

    @abstractmethod
    def find_and_parse_odds(self):
        raise NotImplementedError

    @abstractmethod
    def save(self, url, odds):
        raise NotImplementedError

    def start(self):
        logging.info("Starting OddsScraper, fetching URL:s and opening them may take a while!")
        self.window_handler.open_page(self.url)

        urls = self.find_urls()

        self.window_handler.open_tabs(urls)

        while True:
            window_handles = self.driver.window_handles.copy()

            for window_handler in window_handles[1:]:

                self.driver.switch_to.window(window_handler)

                logging.info(f"parsing url: {self.driver.current_url:>5}")

                odds = self.find_and_parse_odds()

                if not odds:
                    logging.info(f"closing game: {self.driver.current_url:>5}")
                    self.window_handler.close_tab()
                    continue

                odds = self.odds_cache.add_new_odds(self.driver.current_url, odds)

                if odds:
                    self.save(self.driver.current_url, odds)

                time.sleep(1)
