import re


def build_status(row, tags=[]):
    date = row['Date'].to_pydatetime().strftime("%d.%m.%Y")
    pollster = row['pollster']
    url = row['url']
    last_poll = "Letzte Umfrage von {} am {}. Daten von {}.".format(pollster, date, url)
    return " ".join([last_poll] + tags)


def extract_value(text):
    if not isinstance(text, str):
        return text

    m = re.match(r'^(\d+)(?:,(\d+))?\s*%?$', text, re.UNICODE)
    if m:
        number = m.group(1)
        if m.group(2) and len(m.group(2)) > 0:
            number += "." + m.group(2)
        return float(number)

    return text


def extract_german_date(text):
    if not isinstance(text, str):
        return text

    m = re.search(r'(\d{1,2}).(\d{1,2}).(\d{4})', text, re.UNICODE)
    if m:
        year = int(m.group(3))
        month = int(m.group(2))
        day = int(m.group(1))
        return f"{year:04}-{month:02}-{day:02}"

    m = re.search(r'(\d{1,2}).\s*(\w+)\s*(\d{4})', text, re.UNICODE)
    if not m:
        return text

    day = int(m.group(1))
    month = m.group(2)
    year = int(m.group(3))

    month_map = {
        'Januar': 1,
        'Februar': 2,
        'März': 3,
        'April': 4,
        'Mai': 5,
        'Juni': 6,
        'Juli': 7,
        'August': 8,
        'September': 9,
        'Oktober': 10,
        'November': 11,
        'Dezember': 12
    }

    if month not in month_map:
        return text

    month_number = month_map[month]

    return f"{year:04}-{month_number:02}-{day:02}"
