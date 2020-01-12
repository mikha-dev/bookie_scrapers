import time


class WindowHandler:
    def __init__(self, webdriver):
        self.webdriver = webdriver

    def open_page(self, url):
        self.webdriver.get(url)
        time.sleep(2)

    def open_tab(self, url, delay=3):
        self.webdriver.execute_script(f"window.open('{url}', '_blank')")

        time.sleep(delay)

    def open_tabs(self, urls: list):
        for url in urls:
            self.open_tab(url)

    def go_to_main_page(self):
        self.webdriver.switch_to.window(self.webdriver.window_handles[0])

    def close_tab(self):
        self.webdriver.close()
