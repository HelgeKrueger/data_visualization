import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column

from election_data import ElectionData

output_file('output/election.html')

def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")

germany = ElectionData(
    'https://www.wahlrecht.de/umfragen/emnid.htm',
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
germany.add_url('https://www.wahlrecht.de/umfragen/forsa.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/allensbach.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/politbarometer.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/gms.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/dimap.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/insa.htm')
germany.add_url('https://www.wahlrecht.de/umfragen/politbarometer.htm')

germany_plot = create_figure()
germany.plot(germany_plot)


european_election = ElectionData(
    'https://www.wahlrecht.de/umfragen/europawahl.htm',
    title='Europawahl')

european_plot = create_figure()
european_election.plot(european_plot)


bremen = ElectionData('https://www.wahlrecht.de/umfragen/landtage/bremen.htm',
                      title='Bremenwahl',
                      parties=['CDU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD'],
                      time_period='30d')

bremen_plot = create_figure()
bremen.plot(bremen_plot)

show(column(germany_plot, european_plot, bremen_plot))
