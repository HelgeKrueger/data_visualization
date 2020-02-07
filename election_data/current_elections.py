import pandas as pd
import sys

from .election_data import ElectionData


available_current_elections = ['germany', 'hamburg', 'thuringia']


def get_current_election_for_name(name):
    if name == 'germany':
        data = CurrentElections.germany()
        tags = ['#btw', '#btw21']
    elif name == 'hamburg':
        data = CurrentElections.hamburg()
        tags = ['#HHWahl', '#ltwhh']
    elif name == 'thuringia':
        data = CurrentElections.thuringia()
        tags = ['#ltwth']
    else:
        print("Unknown election ", name)
        sys.exit(1)

    return data, tags


class CurrentElections:
    @staticmethod
    def germany():
        germany_urls = [
            'https://www.wahlrecht.de/umfragen/emnid.htm',
            'https://www.wahlrecht.de/umfragen/forsa.htm',
            'https://www.wahlrecht.de/umfragen/allensbach.htm',
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

    @staticmethod
    def thuringia():
        return ElectionData(
            'https://www.wahlrecht.de/umfragen/landtage/thueringen.htm',
            title="Umfragen zur Landtagswahl in Thüringen",
            parties=['CDU',
                     'SPD',
                     'GRÜNE',
                     'FDP',
                     'LINKE',
                     'AfD'],
            #      next_election_date=pd.to_datetime('2019-10-27'),
            display_elections=[pd.to_datetime('2019-10-27')],
            results={
                'CDU': 21.7,
                'SPD': 8.2,
                'GRÜNE': 5.2,
                'FDP': 5.0,
                'LINKE': 31.0,
                'AfD': 23.4
            },
            start_date=pd.to_datetime('2019-01-01'),
            filename="tmp_thuringia"
        )
