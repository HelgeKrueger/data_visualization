from .status_list import StatusList


def test_date_format():
    status_list = StatusList()

    dtypes = status_list.data.dtypes

    assert str(dtypes.loc['date']) == 'datetime64[ns]'
