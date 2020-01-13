import datetime
import logging
from pathlib import Path

import pandas as pd


class OddsCache:
    def __init__(self, data_path: Path, competition_name):
        self.data_path = data_path
        self.data_path.mkdir(exist_ok=True, parents=True)
        self.competition_name = competition_name + ".csv"
        self.cache = {}

    @staticmethod
    def add_new_bookies(old_bookies, new_bookies):
        # Add bookies that did not exist previously and save to cache
        updated_df = pd.concat(
            [new_bookies[~new_bookies.index.isin(old_bookies.index)], old_bookies]
        )

        return updated_df

    def add_new_odds(self, url, odds):

        new_updates = self._create_data_frame(odds)

        # If game not yet seen add bookies to cache
        if url not in self.cache:
            self.cache[url] = new_updates
            return

        # Get previously bookies for selected url
        old_updates = self.cache[url]

        self.cache[url] = new_updates

        # calculate the difference between cache and new odds
        difference_df = new_updates[["1", "X", "2"]] - old_updates[["1", "X", "2"]]

        # Get the index of rows that changed since last save
        difference_index = (difference_df > 0).any(axis="columns")

        # Select rows where changes occurred
        difference_df = difference_df.loc[difference_index, :]

        if difference_index.any():
            logging.info(f"odds difference in:  {url}")

        difference_df.columns = ["1Diff", "XDiff", "2Diff"]

        merged_cached_df = new_updates[difference_index].merge(
            difference_df, on="bookie"
        )

        merged_cached_df["url"] = url
        merged_cached_df["fetched"] = datetime.datetime.utcnow()

        if not merged_cached_df.empty:
            merged_cached_df.to_csv(
                self.data_path / self.competition_name, mode="a", header=None, float_format="%.2f"
            )

    @staticmethod
    def _create_data_frame(odds):
        df = pd.DataFrame(odds, columns=["bookie", "1", "X", "2", "payout"])
        df = df.set_index("bookie")
        df = df.astype({"1": float, "X": float, "2": float})
        return df
