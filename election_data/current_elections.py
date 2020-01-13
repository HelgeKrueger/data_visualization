import pandas as pd

from .election_data import ElectionData

class CurrentElections:
    @staticmethod
    def germany():
        germany_urls = [
            'https://www.wahlrecht.de/umfragen/emnid.htm',
            'https://www.wahlrecht.de/umfragen/forsa.htm',
            'https://www.wahlrecht.de/umfragen/allensbach.htm',
            'https://www.wahlrecht.de/umfragen/politbarometer.htm',
            'https://www.wahlrecht.de/umfragen/gms.htm',
            'https://www.wahlrecht.de/umfragen/dimap.htm',
            'https://www.wahlrecht.de/umfragen/insa.htm',
            'https://www.wahlrecht.de/umfragen/politbarometer.htm'
        ]

        return ElectionData(
            germany_urls,
            title='Bundestagswahl',
            parties=[
                'CDU/CSU',
                'SPD',
                'GRÜNE',
                'FDP',
                'LINKE',
                'AfD'],
            date_column='Unnamed: 0',
            time_period='14d',
            next_election_date=pd.to_datetime('2021-10-01'),
            filename="tmp_germany")

    @staticmethod
    def hamburg():
        return ElectionData(
            'https://www.wahlrecht.de/umfragen/landtage/hamburg.htm',
            title="Umfragen zur Bürgerschaftswahl in Hamburg",
            parties=['CDU',
                     'SPD',
                     'GRÜNE',
                     'FDP',
                     'LINKE',
                     'AfD'],
            next_election_date=pd.to_datetime('2020-02-23'),
            start_date=pd.to_datetime('2019-01-01'),
            filename="tmp_hamburg"
        )
