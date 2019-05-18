import pandas as pd

def load_url(url, parties, date_format='%d.%m.%Y', date_column = 'Datum'):
    data = pd.read_html(url)
    polling_data = pd.DataFrame()
    polling_data['Date'] = pd.to_datetime(data[1][date_column], errors='coerce', format=date_format)
    for party in parties:
        polling_data[party] = pd.to_numeric(data[1][party].apply(lambda x: x.split(' ')[0].replace(',', '.')), errors='coerce')

    polling_data = polling_data.dropna()

    polling_data['Idx'] = polling_data['Date']
    polling_data = polling_data.set_index('Idx').sort_index(ascending=True)

    return polling_data
