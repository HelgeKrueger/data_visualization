import pandas as pd

from .election_data import ElectionData


def get_european_election_2019(filename):
    return ElectionData(
        'https://www.wahlrecht.de/umfragen/europawahl.htm',
        title='Europawahl',
        next_election_date=pd.to_datetime('2019-05-26'),
        filename=filename,
        results={
            'CDU': 28.9,
            'SPD': 15.8,
            'GRÜNE': 20.5,
            'FDP': 5.4,
            'LINKE': 5.5,
            'AfD': 11.0})


def get_bremen_election_2019(filename):
    return ElectionData(
        'https://www.wahlrecht.de/umfragen/landtage/bremen.htm',
        title='Bremenwahl',
        parties=['CDU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
        next_election_date=pd.to_datetime('2019-05-26'),
        time_period='30d',
        filename=filename,
        results={
            'CDU': 26.7,
            'SPD': 24.9,
            'GRÜNE': 17.4,
            'FDP': 5.9,
            'LINKE': 11.3,
            'AfD': 6.1})


def get_germany_election_2017(filename):
    return ElectionData([
        'https://www.wahlrecht.de/umfragen/emnid.htm',
        'https://www.wahlrecht.de/umfragen/forsa.htm',
        'https://www.wahlrecht.de/umfragen/allensbach.htm',
        'https://www.wahlrecht.de/umfragen/politbarometer.htm',
        'https://www.wahlrecht.de/umfragen/gms.htm',
        'https://www.wahlrecht.de/umfragen/dimap.htm',
        'https://www.wahlrecht.de/umfragen/insa.htm',
        'https://www.wahlrecht.de/umfragen/politbarometer/politbarometer-2017.htm'],
        title='Bundestagswahl 2017',
        parties=['CDU/CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
        date_column='Unnamed: 0',
        time_period='14d',
        next_election_date=pd.to_datetime('2017-09-24'),
        start_date=pd.to_datetime('2013-09-23'),
        filename=filename,
        results={
        'CDU/CSU': 32.9,
        'SPD': 20.5,
        'GRÜNE': 8.9,
        'FDP': 10.7,
        'LINKE': 9.2,
        'AfD': 12.6
    })


filename_to_election_data_map = {
    '20190526_europa': get_european_election_2019,
    '20190526_bremen': get_bremen_election_2019,
    '20170924_germany': get_germany_election_2017,
}


def get_historic_election_data(filename):
    return filename_to_election_data_map[filename](filename)


def get_historic_elections():
    keys = sorted(filename_to_election_data_map.keys())
    return keys
