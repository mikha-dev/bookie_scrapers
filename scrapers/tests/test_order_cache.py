import functools
import os
import tempfile
from string import ascii_letters, digits
from unittest.mock import Mock

import hypothesis.strategies as st
from hypothesis import given

from scrapers.base.odds_cache import OddsCache

alphabet = ascii_letters + digits + "-_"


def valid_path_names():
    return (st.
            integers(min_value=0, max_value=10)
            .flatmap(lambda i: st.lists(st.text(min_size=1, alphabet=alphabet), min_size=i, max_size=i))
            .map(functools.partial(str.join, "/"))
            )


def valid_bookies():
    return st.text(alphabet=alphabet, min_size=1)


def valid_odds(bookie=valid_bookies()):
    return st.fixed_dictionaries({
        'url': bookie.map(lambda s: "http://oddsportal.com/" + s),
        'bookie': bookie,
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


@given(st.data())
def test_insert(data):
    bookie1, bookie2 = data.draw(valid_bookies()), data.draw(valid_bookies())

    mock_repository = Mock()

    odds_cache = OddsCache(mock_repository)

    odds1 = [data.draw(valid_odds(st.just(bookie1)))]
    odds2 = [data.draw(valid_odds(st.just(bookie2)))]

    if bookie1 == bookie2:

        odds_cache.add(odds1)
        odds_cache.add(odds1)

        assert mock_repository.called_once()
        mock_repository.reset_mock()

        if odds1 != odds2:
            odds_cache.add(odds2)
            assert mock_repository.called
            assert mock_repository.called_with(odds2)

            odds_cache.add(odds1)
            assert mock_repository.called_with(odds1)

    else:
        odds_cache.add(odds2)
        odds_cache.add(odds1)

        assert mock_repository.call_count == 2

        odds3 = data.draw(valid_odds(st.just(bookie1)))

        if odds3 != odds1[0]:
            odds_cache.add([odds3])
            assert mock_repository.called_with(odds3)
        else:
            mock_repository.mock_reset()
            odds_cache.add([odds3])
            assert mock_repository.called
