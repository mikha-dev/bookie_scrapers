import csv
import logging

fields = ["url", "bookie", "1", "X", "2", "payout"]


def csv_repository(odds_difference, data_path="pl.csv"):
    logging.info("Adding odds from bookie: %s, url: %s", odds_difference['bookie'], odds_difference['url'])

    with open(data_path, 'a') as f:
        csv_dict_writer = csv.DictWriter(f, fieldnames=fields)
        csv_dict_writer.writerow(odds_difference)