import functools
from string import ascii_letters, digits
from unittest.mock import Mock

import hypothesis.strategies as st
from hypothesis import given, assume

from scrapers.base.odds_cache import OddsCache

alphabet = ascii_letters + digits + "-_"


def valid_path_names():
    return (st.
            integers(min_value=0, max_value=10)
            .flatmap(lambda i: st.lists(st.text(min_size=1, alphabet=alphabet), min_size=i, max_size=i))
            .map(functools.partial(str.join, "/"))
            )


def valid_bookie_names():
    return st.text(alphabet=alphabet, min_size=1)


def valid_odds(bookie=valid_bookie_names()):
    return st.fixed_dictionaries({
        'url': bookie.map(lambda s: "http://oddsportal.com/" + s),
        'bookie': bookie,
        'home': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'draw': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'away': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'payout': st.floats(min_value=0, max_value=100).map(lambda p: str(round(p, 1)) + "%")
    })


@given(st.data())
def test_insert_same_bookie(data):
    bookie1, bookie2 = data.draw(valid_bookie_names()), data.draw(valid_bookie_names())

    assume(bookie1 != bookie2)

    mock_repository = Mock()
    odds_cache = OddsCache(mock_repository)

    odds1 = [data.draw(valid_odds(st.just(bookie1))),
             data.draw(valid_odds(st.just(bookie1))),
             data.draw(valid_odds(st.just(bookie2)))]

    assume(odds1[0] != odds1[1])

    odds_cache.add(odds1)

    assert mock_repository.call_count == 3
