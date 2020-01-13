import pandas as pd
import argparse
from subprocess import call
import sys
import os

from election_data import ElectionData, CurrentElections

from apiio import Twitter

parser = argparse.ArgumentParser('')
parser.add_argument('--notweet', action='store_true')
args = parser.parse_args()

germany = CurrentElections.germany()

if not germany.refresh():
    print("")
    print("-" * 80)
    print("No new data")
    sys.exit(1)

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

