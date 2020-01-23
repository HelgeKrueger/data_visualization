import pandas as pd
import argparse
from subprocess import call
import sys
import os

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.io import export_png

from election_data import ElectionData

from apiio import Twitter

parser = argparse.ArgumentParser('')
parser.add_argument('--notweet', action='store_true')
args = parser.parse_args()

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

tmp_filename = 'tmp_germany.csv'

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

germany_old = ElectionData(
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
    filename=tmp_filename)

if len(germany.data) == len(germany_old.data):
    print("")
    print("-" * 80)
    print("No new data")
    sys.exit(1)

germany.save(os.join('data', tmp_filename))

filename = 'germany.png'
germany.plot_to_file(filename)


last_row = germany.get_last().iloc[0]


def build_status(row):
    date = row['Date'].to_pydatetime().strftime("%d.%m.%Y")
    pollster = row['pollster']
    url = row['url']
    return "Letzte Umfrage von {} am {}. Daten von {}.".format(pollster, date, url)


print(build_status(last_row))

if args.notweet:
    call(["xdg-open", filename])

if not args.notweet:
    twitter = Twitter()
    twitter.auth()

    twitter.post_file(filename, status=build_status(last_row))

