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
