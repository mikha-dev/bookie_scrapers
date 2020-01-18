import csv
import logging
from datetime import datetime

fields = ["url", "bookie", "1", "X", "2", "payout", "publish_time"]


def csv_repository(odds_difference, path="pl.csv"):
    logging.info("Adding odds from bookie: %s, url: %s", odds_difference['bookie'], odds_difference['url'])
    odds_difference = odds_difference.copy()
    odds_difference['publish_time'] = datetime.utcnow().isoformat()

    with open(path, 'a') as f:
        csv_dict_writer = csv.DictWriter(f, fieldnames=fields)
        csv_dict_writer.writerow(odds_difference)
