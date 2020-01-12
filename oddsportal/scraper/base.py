from selenium import webdriver

from oddsportal.windowhandler import WindowHandler


class BaseScraper:
    def __init__(self, url: str, headless=False):
        self.url = url
        self.driver = self._initialize_driver(headless)
        self.window_handler = WindowHandler(self.driver)

    @staticmethod
    def _initialize_driver(headless):
        options = webdriver.ChromeOptions()

        options.add_argument("--disable-gpu")

        if headless:
            options.add_argument("--headless")

        # options.add_argument("user-data-dir=./profiles/" + self.profile_path)

        options.set_capability(
            "perfLoggingPrefs", {"enableNetwork": False, "enablePage": False}
        )

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-setuid-sandbox")

        driver = webdriver.Chrome(options=options)

        return driver

    def start(self):
        raise NotImplementedError
