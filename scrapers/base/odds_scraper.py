import logging
import time
from abc import abstractmethod

from scrapers.base.base import BaseScraper


class OddsScraper(BaseScraper):

    def __init__(self, url: str, callback):
        super().__init__(url)
        self.callback = callback

    @abstractmethod
    def find_urls(self):
        raise NotImplementedError

    @abstractmethod
    def find_and_parse_odds(self):
        raise NotImplementedError

    def start(self):
        logging.info("Starting OddsScraper, fetching URL:s and opening them may take a while!")
        self.window_handler.open_page(self.url)

        urls = self.find_urls()[:1]

        self.window_handler.open_tabs(urls)

        while True:
            window_handles = self.driver.window_handles.copy()

            for window_handler in window_handles[1:]:

                self.driver.switch_to.window(window_handler)

                logging.info(f"parsing url: {self.driver.current_url:>5}")

                odds = self.find_and_parse_odds()

                if odds:
                    self.callback(odds)
                    time.sleep(1)
                    continue

                if isinstance(odds, str):
                    logging.info(f"closing game: {self.driver.current_url:>5}")
                    self.window_handler.close_tab()
                    continue
