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
        plt.figure(figsize=(16, 8))

        smoothed = self.election_data.smoothed_daily_data()

        for party in self.election_data.parties:
            plt.plot(self.election_data.data['Date'], self.election_data.data[party], 'o', color=party_to_color[party], alpha=0.3)

            # line, = plt.plot(self.election_data.data['Date'], self.election_data.data[party + '_mean'], '-', color=party_to_color[party])
            line, = plt.plot(smoothed['Date'], smoothed[party], '-', color=party_to_color[party])
            line.set_label(party)

        if self.election_data.next_election_date:
            plt.axvline(x=self.election_data.next_election_date)

        for date in self.election_data.display_elections:
            plt.axvline(x=date)

        if self.election_data.results:
            self.plot_result()

        plt.legend(loc='upper left')
        plt.ylim(0, None)

        plt.savefig(filename, bbox_inches='tight')

    def plot_result(self):
        results = self.election_data.results
        for party in results:
            plt.axhline(y=results[party], color=party_to_color[party], linestyle='dashed')
