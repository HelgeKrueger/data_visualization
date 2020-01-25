from .historic import get_historic_election_data


def test_smoothed_daily_data():
    data = get_historic_election_data('20170924_germany')

    result = data.smoothed_daily_data()

    assert len(result) > 1000
    assert list(result.columns) == ['Date', 'CDU/CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD']
