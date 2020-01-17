# import logging
#
# from scrapers.oddsportal.oddsportal import OddsPortal
# logging.basicConfig(level=logging.INFO)
#
# config = {
#     "url": "https://www.oddsportal.com/soccer/england/premier-league/",
#     "data_path": "./data",
#     "competition_name": "premier-league"
# }
#
# premier_league_scraper = OddsPortal(**config)
# premier_league_scraper.start()
from scrapers.base.odds_cache import OddsCache

OddsCache(lambda: None, "./a")
