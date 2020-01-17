from collections import defaultdict


class OddsCache:
    def __init__(self, repository_callback):
        """
        Args:
            data_path (str): Optional, if specified will create directory specified
            repository_callback: Method which will receive a list of odds difference
        """
        assert repository_callback, "Add callback that will retrieve odds differences"

        self.cache = defaultdict(dict)
        self.repository_callback = repository_callback

    def add(self, odds: list):
        for o in odds:
            cached_odds = self.cache[o['url']].get(o['bookie'])

            if not cached_odds:
                self.cache[o['url']][o['bookie']] = o
                self.repository_callback(o)
            else:
                if cached_odds != o:
                    self.cache[o['url']][o['bookie']] = o
                    self.repository_callback(o)
