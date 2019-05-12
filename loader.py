import pandas as pd

def load_url(url, parties):
    data = pd.read_html(url)
    polling_data = pd.DataFrame()
    polling_data['Date'] = pd.to_datetime(data[1]['Unnamed: 0'], errors='coerce')
    for party in parties:
        polling_data[party] = pd.to_numeric(data[1][party].apply(lambda x: x.split(' ')[0].replace(',', '.')), errors='coerce')
    polling_data.head()

    return polling_data
