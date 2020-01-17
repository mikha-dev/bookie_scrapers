import logging

from scrapers.oddsportal.oddsportal import OddsPortal
logging.basicConfig(level=logging.INFO)

config = {
    "url": "https://www.oddsportal.com/soccer/england/premier-league/",
    "data_path": "./data",
    "competition_name": "premier-league"
}

OddsPortal(**config).start()
