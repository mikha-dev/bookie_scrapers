from pathlib import Path

from oddsportal.odds_cache import OddsCache
from oddsportal.scraper.odds_scraper import OddsScraper


class OddsPortal:

    def __init__(self, config):
        self.config = config

    def start_scraper(self):
        data_path = Path(self.config['data_path'])
        odds_cache = OddsCache(data_path, self.config['competition_name'])
        odds_scraper = OddsScraper(self.config['url'], odds_cache)
        odds_scraper.start()
