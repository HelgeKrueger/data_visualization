import argparse
import sys
from subprocess import Popen

from election_data import get_current_election_for_name, available_current_elections
from apiio import Twitter
from lib import build_status

parser = argparse.ArgumentParser('')
parser.add_argument('--election', default='germany', help="Available elections: " + ", ".join(available_current_elections))
parser.add_argument('--notweet', action='store_true')
parser.add_argument('--ignore_update', action='store_true')
args = parser.parse_args()


data, tags = get_current_election_for_name(args.election)

print()
print("Processing election for", args.election)
print()

if not args.ignore_update and not data.refresh():
    print("no new data")
    sys.exit(1)

filename = 'output/tmp.png'

data.plot_to_file(filename)
last_row = data.get_last().iloc[0]

if args.notweet:
    Popen("xdg-open {}".format(filename), shell=True)

if not args.notweet:
    twitter = Twitter()
    twitter.auth()

    twitter.post_file(filename, status=build_status(last_row, tags=tags))
