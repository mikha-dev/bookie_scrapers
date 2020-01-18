# import functools
import logging
# from scrapers.oddsportal import OddsPortal
# from scrapers.repositories import csv_repository

logging.basicConfig(level=logging.INFO)

import functools

from scrapers.base.odds_cache import OddsCache
from scrapers.oddsportal import OddsPortal
from scrapers.repositories import csv_repository

portal = OddsPortal(
    url="https://www.oddsportal.com/soccer/england/premier-league/",
    callback=functools.partial(csv_repository, path='data/pl.csv')
).start()

# portal.driver.get("https://www.oddsportal.com/soccer/england/premier-league/watford-tottenham-rZddfGpp/")
# o1 = portal.find_and_parse_odds()
# portal.odds_cache.add(o1)
#
# o2 = [o.copy() for o in o1]
# o2[0].update({'1': 1.01})
# portal.odds_cache.add(o2)
# portal.odds_cache.add(o1)
#
# for o1, o2 in zip(o1, o2):
#     print(o1['1'], o2['1'], o1 == o2)

