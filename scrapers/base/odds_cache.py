from collections import defaultdict
from functools import wraps


def odds_cache(func):
    cache = defaultdict(dict)

    @wraps(func)
    def add(odds: list, **kwargs):
        for o in odds:
            cached_odds = cache[o['url']].get(o['bookie'])

            if not cached_odds:
                cache[o['url']][o['bookie']] = o
                func(o, **kwargs)
            else:
                if cached_odds != o:
                    cache[o['url']][o['bookie']] = o
                    func(o, **kwargs)

    return add
