import pandas as pd
from .historic import GermanyElectionResultLookup


def test_get_germany_result():
    lookup = GermanyElectionResultLookup()
    data = lookup.lookup('2011-02-20')

    assert data is not None
    assert data['Date'] == pd.to_datetime('2011-02-20')
