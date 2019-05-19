import pandas as pd

def load_url(url, parties, date_format='%d.%m.%Y', date_column = 'Datum'):
    data = pd.read_html(url)
    raw_data = data[1]
    raw_keys = raw_data.keys()

    if date_column not in raw_keys:
        if 'Datum' in raw_keys:
            date_column = 'Datum'
        else:
            print("Cannot find date_column ", date_column, " in keys: ", raw_keys)


    polling_data = pd.DataFrame()
    polling_data['Date'] = pd.to_datetime(raw_data[date_column], errors='coerce', format=date_format)
    for party in parties:
        polling_data[party] = pd.to_numeric(raw_data[party].apply(lambda x: x.split(' ')[0].replace(',', '.')), errors='coerce')

    polling_data = polling_data.dropna()

    polling_data['Idx'] = polling_data['Date']
    polling_data = polling_data.set_index('Idx').sort_index(ascending=True)

    return polling_data
