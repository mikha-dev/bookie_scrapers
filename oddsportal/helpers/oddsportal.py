import logging

from selenium.common.exceptions import NoSuchElementException


def find_urls(webdriver):

    """
    Finds all non active urls for a specific league.
    """

    urls = webdriver.find_elements_by_xpath(
        "//tr[not(contains(@class, 'deactivate'))]/td[@class='name table-participant']/a"
    )

    urls = list(filter(lambda url: url.get_attribute("href").startswith("https"), urls))

    urls = [url.get_attribute("href") for url in urls]

    return urls


def get_new_urls(self):

    new_urls = list(set(self._find_urls()) - self.current_urls)

    for url in new_urls:
        self.current_urls.add(url)

    return new_urls


def parse_odds(driver):
    try:
        finished = driver.find_element_by_xpath("//div[@id='event-status']").text

        if len(finished.strip()) > 0:
            return "FINISHED"

        odds = driver.find_elements_by_xpath("//tr[contains(@class, 'lo')]")
        odds = [list(map(lambda s: s.strip(), o.text.split("\n"))) for o in odds]
        odds = [o for o in odds if len(o) == 5]
        return odds

    except NoSuchElementException as _:
        pass
