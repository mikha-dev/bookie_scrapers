import functools
import logging

from scrapers.oddsportal import OddsPortal
from scrapers.repositories import csv_repository

logging.basicConfig(level=logging.INFO)


portal = OddsPortal(
    url="https://www.oddsportal.com/soccer/england/premier-league/",
    callback=functools.partial(csv_repository, path='data/pl.csv')
).start()