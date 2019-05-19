import pandas as pd

from bokeh.models import ColumnDataSource

from loader import load_url

class ElectionData():
    def __init__(self, url, parties=['CDU', 'SPD', 'GRÜNE','FDP', 'LINKE' , 'AfD'],
            start_date=pd.to_datetime('2018-01-01'),
            time_period='30d',
            date_column='Datum'):

        self.parties = parties
        self.start_date = start_date
        self.date_column = date_column

        self.data = load_url(url, parties, date_column=date_column)

        date_filter = self.data['Date'] > self.start_date
        self.data = self.data[date_filter]

        self._add_statistics()


    def add_url(self, url):
        new_data = load_url(url, self.parties, date_column=self.date_column)
        self.data = pd.concat([self.data, new_data], sort=True).sort_index(ascending=True)

        date_filter = self.data['Date'] > self.start_date
        self.data = self.data[date_filter]

        self._add_statistics()

    def _add_statistics(self):
        for party in self.parties:
            self.data[party + '_mean'] = self.data[party].rolling('30d').mean()
            self.data[party + '_std'] = self.data[party].rolling('30d').std()
            self.data[party + '_low'] = self.data[party + '_mean'] - self.data[party + '_std']
            self.data[party + '_up'] = self.data[party + '_mean'] + self.data[party + '_std']

    def asColumnDataSource(self):
        return ColumnDataSource(self.data.reset_index())

