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


def get_bayern_election_2018(filename):
    return ElectionData(
        'https://www.wahlrecht.de/umfragen/landtage/bayern.htm',
        title='Bayernwahl 2018',
        parties=['CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'FW', 'AfD'],
        next_election_date=pd.to_datetime('2018-10-14'),
        start_date=pd.to_datetime('2013-09-16'),
        time_period='30d',
        filename=filename,
        results={
            'CSU': 37.2,
            'SPD': 9.7,
            'GRÜNE': 17.6,
            'FDP': 5.1,
            'LINKE': 3.2,
            'FW': 11.6,
            'AfD': 10.2})


def get_hessen_election_2018(filename):
    return ElectionData(
        'https://www.wahlrecht.de/umfragen/landtage/hessen.htm',
        title='Hessenwahl 2018',
        parties=['CDU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
        next_election_date=pd.to_datetime('2018-10-28'),
        start_date=pd.to_datetime('2013-09-23'),
        time_period='30d',
        filename=filename,
        results={
            'CDU': 27.0,
            'SPD': 19.8,
            'GRÜNE': 19.8,
            'FDP': 7.5,
            'LINKE': 6.3,
            'AfD': 13.1})


def get_germany_election_2017(filename):
    return ElectionData([
        'https://www.wahlrecht.de/umfragen/emnid.htm',
        'https://www.wahlrecht.de/umfragen/forsa.htm',
        'https://www.wahlrecht.de/umfragen/allensbach.htm',
        'https://www.wahlrecht.de/umfragen/yougov.htm',
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


def get_germany_election_2013(filename):
    return ElectionData([
        'https://www.wahlrecht.de/umfragen/emnid/2013.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2013.htm',
        'https://www.wahlrecht.de/umfragen/allensbach/2013.htm',
        'https://www.wahlrecht.de/umfragen/gms.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2013.htm',
        'https://www.wahlrecht.de/umfragen/insa.htm',
        'https://www.wahlrecht.de/umfragen/yougov.htm',
        'https://www.wahlrecht.de/umfragen/politbarometer/politbarometer-2013.htm'],
        title='Bundestagswahl 2013',
        parties=['CDU/CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
        date_column='Unnamed: 0',
        time_period='14d',
        next_election_date=pd.to_datetime('2013-09-22'),
        start_date=pd.to_datetime('2009-09-28'),
        filename=filename,
        results={
        'CDU/CSU': 41.5,
        'SPD': 25.7,
        'GRÜNE': 8.4,
        'FDP': 4.8,
        'LINKE': 8.6,
        'AfD': 4.7
    })


def get_germany_election_2009(filename):
    return ElectionData([
        'https://www.wahlrecht.de/umfragen/emnid/2013.htm',
        'https://www.wahlrecht.de/umfragen/emnid/2008.htm',
        'https://www.wahlrecht.de/umfragen/emnid/2007.htm',
        'https://www.wahlrecht.de/umfragen/emnid/2006.htm',
        'https://www.wahlrecht.de/umfragen/emnid/2005.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2013.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2008.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2007.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2006.htm',
        'https://www.wahlrecht.de/umfragen/forsa/2005.htm',
        'https://www.wahlrecht.de/umfragen/allensbach/2009.htm',
        'https://www.wahlrecht.de/umfragen/politbarometer/politbarometer-2009.htm',
        'https://www.wahlrecht.de/umfragen/gms/projektion-2009.htm',
        'https://www.wahlrecht.de/umfragen/gms.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2013.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2008.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2007.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2006.htm',
        'https://www.wahlrecht.de/umfragen/dimap/2005.htm'
    ],
        title='Bundestagswahl 2009',
        parties=['CDU/CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
        date_column='Unnamed: 0',
        time_period='14d',
        next_election_date=pd.to_datetime('2009-09-27'),
        start_date=pd.to_datetime('2005-09-19'),
        filename=filename,
        results={
        'CDU/CSU': 33.8,
        'SPD': 23.0,
        'GRÜNE': 10.7,
        'FDP': 14.6,
        'LINKE': 11.9,
        'AfD': 0
    })


filename_to_election_data_map = {
    '20190526_europa': get_european_election_2019,
    '20181014_bayern': get_bayern_election_2018,
    '20190526_bremen': get_bremen_election_2019,
    '20181028_hessen': get_hessen_election_2018,
    '20170924_germany': get_germany_election_2017,
    '20130922_germany': get_germany_election_2013,
    '20090927_germany': get_germany_election_2009,
}


def get_historic_election_data(filename):
    return filename_to_election_data_map[filename](filename)


def get_historic_elections():
    keys = sorted(filename_to_election_data_map.keys())
    return keys


def get_germany_result(date):
    date = pd.to_datetime(date)
    for key in filename_to_election_data_map:
        if key.endswith('_germany'):
            data = get_historic_election_data(key).smoothed_daily_data()
            if date in data['Date']:
                return data.loc[date]
