import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column

from election_data import ElectionData

output_file('output/election.html')


def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")


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


germany = ElectionData(
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
    next_election_date=pd.to_datetime('2021-10-01'))

germany_plot = create_figure()
germany.plot(germany_plot)


def bundesland(
        url,
        title,
        parties,
        next_election_date=None,
        time_period='30d'):
    data = ElectionData(
        url,
        title=title,
        parties=parties,
        next_election_date=next_election_date,
        time_period=time_period)

    plot = create_figure()
    data.plot(plot)

    return plot


brandenburg_plot = bundesland(
    'https://www.wahlrecht.de/umfragen/landtage/brandenburg.htm',
    'Brandenburg',
    [
        'CDU',
        'SPD',
        'GRÜNE',
        'FDP',
        'LINKE',
        'AfD'],
    next_election_date=pd.to_datetime('2019-09-01'))
sachsen_plot = bundesland(
    'https://www.wahlrecht.de/umfragen/landtage/sachsen.htm',
    'Sachen',
    [
        'CDU',
        'SPD',
        'GRÜNE',
        'FDP',
        'LINKE',
        'AfD'],
    next_election_date=pd.to_datetime('2019-09-01'))
thueringen_plot = bundesland(
    'https://www.wahlrecht.de/umfragen/landtage/thueringen.htm',
    'Thueringen',
    [
        'CDU',
        'SPD',
        'GRÜNE',
        'FDP',
        'LINKE',
        'AfD'],
    next_election_date=pd.to_datetime('2019-10-27'))


show(column(germany_plot, brandenburg_plot, sachsen_plot, thueringen_plot))
