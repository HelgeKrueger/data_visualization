import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column

from election_data import ElectionData, get_historic_election_data, get_historic_elections

output_file('output/history.html')


def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")

plots = []
for election in get_historic_elections():
    data = get_historic_election_data(election)
    plot = create_figure()
    data.plot(plot)
    plots.append(plot)

show(column(plots))
