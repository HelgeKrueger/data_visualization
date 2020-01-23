import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from bokeh.models import ColumnDataSource

from election_data import get_historic_election_data, get_historic_elections, party_to_color

output_file('output/history.html')


def create_figure():
    return figure(plot_width=1024, plot_height=600, x_axis_type="datetime")


plots = []
diffs = []

for election in get_historic_elections():
    data = get_historic_election_data(election)
    plot = create_figure()
    data.plot(plot)
    plots.append(plot)
    diffs.append(data.compute_diff_to_election_as_dataframe())


aggregated_diffs = pd.concat(diffs, ignore_index=True, sort=False)
party_keys = [k for k in aggregated_diffs.keys(
) if k != 'election' and not k.endswith('_std')]

plot = figure(
    plot_width=1024,
    plot_height=600,
    x_range=aggregated_diffs['election'].tolist())

source_df = aggregated_diffs[party_keys].fillna(0).abs()
source_df['election'] = aggregated_diffs['election']

source = ColumnDataSource(source_df)

for party in party_keys:
    plot.circle('election', party, source=source, color=party_to_color[party])

plot.title.text = 'Absolute value of election result - averaged polling'

plots.append(plot)

print("-" * 100)
print("Difference aggregated diff to election result")
print("")
print(aggregated_diffs[['election'] + party_keys])
print("")

difference = pd.DataFrame()
difference['election'] = aggregated_diffs['election']
for party in party_keys:
    difference[party] = (source_df[party] -
                         aggregated_diffs[party + '_std']).abs()

print("-" * 100)
print("Difference aggregated diff to election result adjusted to standard variation")
print("")
print(difference)
print("")
print("Number of differences > 3", (difference[party_keys] > 3).sum().sum())

print("-" * 100)
print("Maximal difference by party")
print("")
print(aggregated_diffs[party_keys].fillna(0).abs().max())

show(column(plots))
