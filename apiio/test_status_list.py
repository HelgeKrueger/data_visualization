import pytest
import os

from .status_list import StatusList


@pytest.mark.skipif(not os.path.exists('data/wahlrecht_twitter.csv'), reason='requires data file')
def test_date_format():
    status_list = StatusList()

    dtypes = status_list.data.dtypes

    assert str(dtypes.loc['date']) == 'datetime64[ns]'
