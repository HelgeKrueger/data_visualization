import argparse
import pandas as pd
import argparse
import sys
from subprocess import call

from election_data import ElectionData
from apiio import Twitter

parser = argparse.ArgumentParser('')
parser.add_argument('--notweet', action='store_true')
args = parser.parse_args()


data = ElectionData(
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
# start_date=pd.to_datetime('2015-02-16')

if not data.refresh():
    print("no new data")
    sys.exit(1)

filename = 'hamburg.png'

data.plot_to_file(filename)

last_row = data.get_last().iloc[0]


def build_status(row):
    date = row['Date'].to_pydatetime().strftime("%d.%m.%Y")
    pollster = row['pollster']
    url = row['url']
    return "Letzte Umfrage von {} am {}. Daten von {}. #HHWahl #ltwhh".format(pollster, date, url)


print(build_status(last_row))

if args.notweet:
    call(["xdg-open", filename])

if not args.notweet:
    twitter = Twitter()
    twitter.auth()

    twitter.post_file(filename, status=build_status(last_row))
