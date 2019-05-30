import pandas as pd
import os

from pathlib import Path

from bokeh.models import Band, ColumnDataSource, Span

from loader import load_url


class ElectionData():
    def __init__(
            self,
            url,
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
            party_to_color={
                'CDU/CSU': 'black',
                'CDU': 'black',
                'SPD': 'red',
                'GRÜNE': 'green',
                'FDP': 'yellow',
                'AfD': 'blue',
                'LINKE': 'purple'},
            title='Election Data',
            next_election_date=None,
            filename=None,
            results=None):

        self.parties = parties
        self.party_to_color = party_to_color
        self.start_date = start_date
        self.date_column = date_column
        self.next_election_date = next_election_date
        self.url = url
        self.title = title
        self.results = results

        if filename:
            self._lazy_load(filename)
        else:
            self._load()

        self._add_statistics()

    def _load(self):
        self.data = load_url(
            self.url,
            self.parties,
            date_column=self.date_column)

        date_filter = self.data['Date'] > self.start_date
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

        date_filter = self.data['Date'] > self.start_date
        self.data = self.data[date_filter]

        self._add_statistics()

    def _add_statistics(self):
        for party in self.parties:
            self.data[party + '_mean'] = self.data[party].rolling('30d').mean()
            self.data[party + '_std'] = self.data[party].rolling('30d').std()
            self.data[party + '_low'] = self.data[party +
                                                  '_mean'] - self.data[party + '_std']
            self.data[party + '_up'] = self.data[party +
                                                 '_mean'] + self.data[party + '_std']

    def asColumnDataSource(self):
        return ColumnDataSource(self.data.reset_index())

    def plot(self, figure):
        source = self.asColumnDataSource()
        figure.title.text = self.title

        for party in self.parties:
            color = self.party_to_color[party]
            figure.circle('Date', party, source=source, size=4, color=color)
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
