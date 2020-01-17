import functools
import logging
from scrapers.oddsportal import OddsPortal
from scrapers.repositories import csv_repository

logging.basicConfig(level=logging.INFO)

OddsPortal(
    url="https://www.oddsportal.com/soccer/england/premier-league/",
    repository_callback=functools.partial(csv_repository, data_path='data/pl.csv')
).start()
