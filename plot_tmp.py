import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource

from election_data import ElectionData, get_historic_election_data, get_historic_elections, party_to_color

output_file('output/history.html')


def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")


plots = []
diffs = []

for election in get_historic_elections():
    data = get_historic_election_data(election)
    data.plot_to_file("/tmp/{}.png".format(election))
