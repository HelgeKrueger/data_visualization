import pandas as pd
import argparse
import sys
from subprocess import call

from election_data import CurrentElections
from apiio import Twitter

parser = argparse.ArgumentParser('')
parser.add_argument('--notweet', action='store_true')
args = parser.parse_args()

data = CurrentElections.hamburg()


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
