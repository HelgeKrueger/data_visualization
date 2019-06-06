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

filename_to_election_data_map = {
  '20190526_europa': get_european_election_2019,
  '20190526_bremen': get_bremen_election_2019
}

def get_historic_election_data(filename):
    return filename_to_election_data_map[filename](filename)

def get_historic_elections():
    keys = list(filename_to_election_data_map.keys())
    keys.sort()
    return keys

