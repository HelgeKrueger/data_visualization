import pandas as pd
from .historic import get_germany_result


def test_get_germany_result():
    data = get_germany_result('2011-02-20')

    assert data is not None
    assert data['Date'] == pd.to_datetime('2011-02-20')
