import pandas as pd
import argparse
import sys
from subprocess import Popen

from election_data import CurrentElections
from apiio import Twitter
from lib import build_status

parser = argparse.ArgumentParser('')
parser.add_argument('--election', default='germany')
parser.add_argument('--notweet', action='store_true')
parser.add_argument('--ignore_update', action='store_true')
args = parser.parse_args()

election = args.election
tags = []

if election == 'germany':
    data = CurrentElections.germany()
elif election == 'hamburg':
    data = CurrentElections.hamburg()
    tags=['#HHWahl', '#ltwhh']
else:
    print("Unknown election ", election)
    sys.exit(1)

print()
print("Processing election for", election)
print()

if not args.ignore_update and not data.refresh():
    print("no new data")
    sys.exit(1)

filename = 'tmp.png'

data.plot_to_file(filename)
last_row = data.get_last().iloc[0]

if args.notweet:
    Popen("xdg-open {}".format(filename), shell=True)

if not args.notweet:
    twitter = Twitter()
    twitter.auth()

    twitter.post_file(filename, status=build_status(last_row, tags=tags))
