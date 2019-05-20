import pandas as pd

from bokeh.models import Band, ColumnDataSource

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
            title='Election Data'):

        self.parties = parties
        self.party_to_color = party_to_color
        self.start_date = start_date
        self.date_column = date_column

        self.title = title

        self.data = load_url(url, parties, date_column=date_column)

        date_filter = self.data['Date'] > self.start_date
        self.data = self.data[date_filter]

        self._add_statistics()

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

        bands = {}

        for party in self.parties:
            color = self.party_to_color[party]
            figure.circle('Date', party, source=source, size=4, color=color)
            figure.line('Date', party + '_mean', source=source, color=color)

            bands[party] = Band(
                base='Date',
                lower=party + '_low',
                upper=party + '_up',
                source=source,
                level='underlay',
                fill_alpha=0.2,
                line_width=1,
                fill_color=color)

            figure.add_layout(bands[party])

        return figure
