import functools
import os
import tempfile
from string import ascii_letters, digits
from unittest.mock import Mock

import hypothesis.strategies as st
from hypothesis import given

from scrapers.base.odds_cache import OddsCache
from scrapers.repositories import csv_repository

fields = ["bookie", "1", "X", "2", "payout"]

alphabet = ascii_letters + digits + "-_"


def valid_path_names():
    ints = st.integers(min_value=0, max_value=10)

    return (ints
            .flatmap(lambda i: st.lists(st.text(min_size=1, alphabet=alphabet), min_size=i, max_size=i))
            .map(functools.partial(str.join, "/"))
            )


def valid_bookies():
    return st.text(alphabet)


def valid_odds():
    return st.fixed_dictionaries({
        'bookie': st.text(alphabet=alphabet, min_size=1),
        'home': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'draw': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'away': st.floats(min_value=0, max_value=1000).map(functools.partial(round, ndigits=2)),
        'payout': st.floats(min_value=0, max_value=100).map(lambda p: str(round(p, 1)) + "%")
    })

    # ['bookie', 'home', 'draw', 'away', 'payout', 'homeDiff', 'drawDiff', 'awayDiff', 'url']


@given(valid_path_names())
def test_create_output_path(path):
    with tempfile.TemporaryDirectory() as tmp_path:

        path = os.path.join(tmp_path, path)
        OddsCache(lambda: None, path)
        assert os.path.exists(path)

        # Check that existing path exist
        OddsCache(lambda: None, path)
        assert os.path.exists(path)


@given(valid_odds())
def test_insert(odds):
    mock_repository = Mock()

    odds_cache = OddsCache(mock_repository)
    odds_cache.add(odds)

    mock_repository.assert_called_with(odds)
