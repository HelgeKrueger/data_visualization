import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column

from election_data import ElectionData

output_file('output/history.html')


def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")


european_election = ElectionData(
    'https://www.wahlrecht.de/umfragen/europawahl.htm',
    title='Europawahl',
    next_election_date=pd.to_datetime('2019-05-26'),
    filename='20190526_europa',
    results={
        'CDU': 28.9,
        'SPD': 15.8,
        'GRÜNE': 20.5,
        'FDP': 5.4,
        'LINKE': 5.5,
        'AfD': 11.0})

european_plot = create_figure()
european_election.plot(european_plot)

bremen_election = ElectionData(
    'https://www.wahlrecht.de/umfragen/landtage/bremen.htm',
    title='Bremenwahl',
    parties=['CDU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
    next_election_date=pd.to_datetime('2019-05-26'),
    time_period='30d',
    filename='20190526_bremen',
    results={
        'CDU': 26.7,
        'SPD': 24.9,
        'GRÜNE': 17.4,
        'FDP': 5.9,
        'LINKE': 11.3,
        'AfD': 6.1})

bremen_plot = create_figure()
bremen_election.plot(bremen_plot)

show(column(european_plot, bremen_plot))
