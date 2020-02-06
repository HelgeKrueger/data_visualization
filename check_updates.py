import sys

from apiio import Twitter, StatusList
from election_data import get_current_election_for_name
from lib import build_status

username = '@wahlrecht_de'


twitter = Twitter()
twitter.auth()

timeline = twitter.timeline(username)
last_entry = timeline[0]

status_list = StatusList()
print(last_entry)

is_new = status_list.check_new(username, last_entry)

if not is_new:
    print("No new entry")
    sys.exit(1)

print("New entry")
print(status_list.data.iloc[0].text)
print()
print('*' * 70)

status_list.save()

for election in ['germany', 'hamburg']:
    data, tags = get_current_election_for_name(election)

    print()
    print("Processing election for", election)
    print()

    if not data.refresh():
        print("no new data for", election)
    else:
        filename = 'output/tmp.png'
        data.plot_to_file(filename)
        last_row = data.get_last().iloc[0]

        twitter = Twitter()
        twitter.auth()

        twitter.post_file(filename, status=build_status(last_row, tags=tags))
