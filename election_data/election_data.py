import pandas as pd
import os

from pathlib import Path

from bokeh.models import Band, ColumnDataSource, Span

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
import seaborn as sns

from .loader import load_url

party_to_color = {
    'CDU/CSU': 'black',
    'CDU': 'black',
    'CSU': 'black',
    'SPD': 'red',
    'GRÜNE': 'green',
    'FDP': 'yellow',
    'AfD': 'blue',
    'FW': 'orange',
    'LINKE': 'purple'}


class ElectionData():
    def __init__(
            self,
            urls,
            parties=[
                'CDU',
                'SPD',
                'GRÜNE',
                'FDP',
                'LINKE',
                'AfD'],
            start_date=pd.to_datetime('2018-01-01'),
            time_period='30d',
            date_column='Datum',
            party_to_color=party_to_color,
            title='Election Data',
            next_election_date=None,
            filename=None,
            results=None):

        self.parties = parties
        self.party_to_color = party_to_color
        self.start_date = start_date
        self.date_column = date_column
        self.next_election_date = next_election_date
        self.time_period = time_period
        if isinstance(urls, list):
            self.urls = urls
        else:
            self.urls = [urls]
        self.title = title
        self.results = results
        self.filename = filename

        if filename:
            self._lazy_load(filename)
        else:
            self._load()

        self._add_statistics()

    def _load(self):
        self.data = load_url(
            self.urls[0],
            self.parties,
            date_column=self.date_column)

        for url in self.urls[1:]:
            self.add_url(url)

        date_filter = self.data['Date'] > self.start_date
        self.data = self.data[date_filter]

        if self.next_election_date:
            date_filter = self.data['Date'] < self.next_election_date
            self.data = self.data[date_filter]

    def _lazy_load(self, filename):
        if not filename.endswith('.csv'):
            filename = filename + '.csv'
        filename = os.path.join('data', filename)

        file_path = Path(filename)

        if file_path.is_file():
            data = pd.read_csv(filename)
            data['Date'] = pd.to_datetime(data['Date'])
            data['Idx'] = pd.to_datetime(data['Idx'])
            self.data = data.set_index('Idx').sort_index(ascending=True)
        else:
            self._load()
            self.data.to_csv(filename)

    def add_url(self, url):
        new_data = load_url(url, self.parties, date_column=self.date_column)
        self.data = pd.concat([self.data, new_data],
                              sort=True).sort_index(ascending=True)

    def _add_statistics(self):
        for party in self.parties:
            rolling = self.data[party].rolling(self.time_period)
            self.data[party + '_mean'] = rolling.mean()
            self.data[party + '_std'] = rolling.std()
            self.data[party + '_low'] = self.data[party + \
                '_mean'] - self.data[party + '_std']
            self.data[party + '_up'] = self.data[party + \
                '_mean'] + self.data[party + '_std']

    def asColumnDataSource(self):
        return ColumnDataSource(self.data.reset_index())

    def plot_to_file(self, filename):
        plt.title(self.title)

        for party in self.parties:
            plt.plot(self.data['Date'], self.data[party], 'o', color=party_to_color[party], alpha=0.2)
            plt.plot(self.data['Date'], self.data[party + '_mean'], '-', color=party_to_color[party])

        if self.next_election_date:
            plt.axvline(x=self.next_election_date)

        plt.savefig(filename)


    def plot(self, figure):
        source = self.asColumnDataSource()
        figure.title.text = self.title

        for party in self.parties:
            color = self.party_to_color[party]
            figure.circle('Date', party, source=source, size=4, color=color, alpha=0.1)
            figure.line('Date', party + '_mean', source=source, color=color)

            band = Band(
                base='Date',
                lower=party + '_low',
                upper=party + '_up',
                source=source,
                level='underlay',
                fill_alpha=0.2,
                line_width=1,
                fill_color=color)
            figure.add_layout(band)

            if self.results:
                election_result = Span(
                    location=self.results[party],
                    dimension='width',
                    line_color=color,
                    line_width=2)
                figure.add_layout(election_result)

        self._plot_next_election(figure)
        self._plot_today(figure)

        return figure

    def _plot_next_election(self, figure):
        if self.next_election_date:
            vline = Span(
                location=self.next_election_date,
                dimension='height',
                line_color='red',
                line_width=3)

            figure.add_layout(vline)
            figure.circle([self.next_election_date], [0])

    def _plot_today(self, figure):
        vline = Span(
            location=pd.datetime.now(),
            dimension='height',
            line_color='black',
            line_width=1,
            line_dash='dashed')

        figure.add_layout(vline)

    def _get_last_mean(self, party):
        return self.data.tail(1)[party + '_mean'].tolist()[0]

    def _get_last_std(self, party):
        return self.data.tail(1)[party + '_std'].tolist()[0]

    def compute_diff_to_election_as_dataframe(self):
        diff = {'election': self.filename}
        for party in self.parties:
            diff[party] = [self.results[party] - self._get_last_mean(party)]
            diff[party + '_std'] = self._get_last_std(party)

        return pd.DataFrame.from_dict(diff)
