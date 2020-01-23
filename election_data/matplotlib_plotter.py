import pandas as pd

import matplotlib
import matplotlib.pyplot as plt

from .constants import party_to_color

matplotlib.use('Agg')
matplotlib.style.use('ggplot')


class MatplotlibPlotter:
    def __init__(self, election_data):
        self.election_data = election_data

    def plot(self, filename):
        plt.title(self.election_data.title)

        smoothed = self.build_line_data()

        for party in self.election_data.parties:
            plt.plot(self.election_data.data['Date'], self.election_data.data[party], 'o', color=party_to_color[party], alpha=0.1)

            # line, = plt.plot(self.election_data.data['Date'], self.election_data.data[party + '_mean'], '-', color=party_to_color[party])
            line, = plt.plot(smoothed['Date'], smoothed[party], '-', color=party_to_color[party])
            line.set_label(party)

        if self.election_data.next_election_date:
            plt.axvline(x=self.election_data.next_election_date)

        plt.legend(loc='upper left')
        plt.ylim(0, None)

        plt.savefig(filename, bbox_inches='tight')

    def build_line_data(self):
        df = self.election_data.data.copy()
        df = df[~df.index.duplicated()]
        min_date = df['Date'].min()
        max_date = df['Date'].max()

        index_daily = pd.date_range(min_date, max_date, freq='1D')
        df = df.reindex(index=index_daily).interpolate('linear')

        result = pd.DataFrame()
        result['Date'] = df.index
        result['Idx'] = df.index
        result = result.set_index('Idx').sort_index(ascending=True)

        for party in self.election_data.parties:
            result[party] = df[party + '_mean'].rolling('14d').mean()

        return result
