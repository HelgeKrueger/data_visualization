import pandas as pd
import re
import time


def parse_string(string):
    if isinstance(string, str):
        return string.split(' ')[0].replace(',', '.')

    print(string)

    return string


def get_pollster_from_url(url):
    m = re.search(r'/(\w+)\.htm', url)
    if not m:
        return
    return m.group(1)


def load_url(url, parties, date_format='%d.%m.%Y', date_column='Datum'):
    print("Loading ... ", url)
    start_time = time.time()
    data = pd.read_html(url, decimal=',', thousands='#')
    raw_data = data[1]
    raw_keys = raw_data.keys()

    if date_column not in raw_keys:
        if 'Datum' in raw_keys:
            date_column = 'Datum'
        else:
            print(
                "Cannot find date_column ",
                date_column,
                " in keys: ",
                raw_keys)

    polling_data = pd.DataFrame()
    polling_data['Date'] = pd.to_datetime(
        raw_data[date_column],
        errors='coerce',
        format=date_format)
    for party in parties:
        polling_data[party] = pd.to_numeric(
            raw_data[party].apply(parse_string), errors='coerce')

    if 'Auftraggeber' in raw_data:
        polling_data['pollster'] = raw_data['Auftraggeber']
    else:
        pollster = get_pollster_from_url(url)
        if pollster:
            polling_data['pollster'] = pollster

    polling_data = polling_data.dropna()

    polling_data['Idx'] = polling_data['Date']
    polling_data = polling_data.set_index('Idx').sort_index(ascending=True)
    print("Done in ", time.time() - start_time, " ms")

    polling_data['url'] = url

    return polling_data
