def build_status(row, tags=[]):
    date = row['Date'].to_pydatetime().strftime("%d.%m.%Y")
    pollster = row['pollster']
    url = row['url']
    last_poll = "Letzte Umfrage von {} am {}. Daten von {}.".format(pollster, date, url)
    return " ".join([last_poll] + tags)
