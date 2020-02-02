import pandas as pd
from collections import defaultdict
from lib.helper import extract_german_date, extract_value
import re
from bs4 import BeautifulSoup
import requests


def split_soup_into_regions(soup):
    data_table = soup.find_all('table')[1]
    lines = data_table.find_all('tr')

    current = "TRASH"
    region_data = defaultdict(list)

    for line in lines:
        if len(line.find_all('th')) == 1:
            current = line.find('th').text
        else:
            region_data[current].append(line)

    return region_data


def convert_data_for_region(data):
    parsed = pd.read_html('<table>' + '\n'.join(map(str, data)) + '</table>')[0]

    if len(parsed) == 0:
        return

    parsed_filter = parsed['Institut(Datum)'].str.contains('Bundestagswahl')

    parsed_filter = parsed_filter.fillna(True)
    parsed = parsed[~parsed_filter]

    columns = parsed.columns

    result = pd.DataFrame()
    result['Date'] = parsed['Institut(Datum)'].map(extract_german_date)
    for party in ['CDU', 'CSU', 'SPD', 'GRÜNE', 'FDP', 'LINKE', 'AfD']:
        if party in columns:
            result[party] = parsed[party].map(extract_value)

    return result


def german_national_polls_by_region():
    page = requests.get('https://www.wahlrecht.de/umfragen/laender.htm')
    soup = BeautifulSoup(page.content, 'html.parser')

    region_data = split_soup_into_regions(soup)

    result = {}

    for k in region_data.keys():
        if k == 'TRASH':
            continue
        name = re.split(r'\s+', k)[0]
        data = convert_data_for_region(region_data[k])
        if len(data) > 0:
            result[name] = data

    return result
