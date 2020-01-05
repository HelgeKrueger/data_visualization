import argparse
import pandas as pd

from election_data import ElectionData
from apiio import Twitter

twitter = Twitter()
twitter.auth()

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
    start_date=pd.to_datetime('2015-02-16')
)

filename = 'hamburg.png'

data.plot_to_file(filename)
twitter.post_file(filename)
