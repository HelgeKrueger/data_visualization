import pandas as pd
import os

class StatusList:
    def __init__(self, filename='data/wahlrecht_twitter.csv'):
        self.filename = filename

        if os.path.exists(filename):
            self.data = pd.read_csv(filename, index_col="index")
        else:
            self.data = pd.DataFrame()

        self.data['date'] = pd.to_datetime(self.data['date'])

    def save(self):
        self.data.to_csv(self.filename, index_label="index")

    def check_new(self, username, status):
        if len(self.data) == 0:
            self.append_entry(username, status)
            return True

        last_row = self.data.tail(1).iloc[0]

        if last_row['username'] == username and last_row['text'] == status['text'] and last_row['date'].to_pydatetime() == status['date']:
            return False

        self.append_entry(username, status)
        return True


    def append_entry(self, username, status):
        self.data = self.data.append({
            'username': username,
            'text': status['text'],
            'date': status['date']
        }, ignore_index=True)

