import logging
import time
from abc import abstractmethod

from scrapers.base.base import BaseScraper
from scrapers.base.odds_cache import OddsCache


class OddsScraper(BaseScraper):

    def __init__(self, url: str, repository_callback):
        super().__init__(url)
        self.odds_cache = OddsCache(repository_callback)

    @abstractmethod
    def find_urls(self):
        raise NotImplementedError

    @abstractmethod
    def find_and_parse_odds(self):
        raise NotImplementedError

    def start(self):
        logging.info("Starting OddsScraper, fetching URL:s and opening them may take a while!")
        self.window_handler.open_page(self.url)

        urls = self.find_urls()[:3]

        self.window_handler.open_tabs(urls)

        while True:
            window_handles = self.driver.window_handles.copy()

            for window_handler in window_handles[1:]:

                self.driver.switch_to.window(window_handler)

                logging.info(f"parsing url: {self.driver.current_url:>5}")

                odds = self.find_and_parse_odds()

                if odds:
                    self.odds_cache.add(odds)
                    continue

                if isinstance(odds, str):
                    logging.info(f"closing game: {self.driver.current_url:>5}")
                    self.window_handler.close_tab()
                    continue

                time.sleep(1.5)
