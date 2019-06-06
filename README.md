# Visualization of available data

My main goal is to understand the data better by visualizating it.

## Polling data in Germany

Data is currently taken from https://www.wahlrecht.de/umfragen/. By running
```
pipenv run python plot.py
```
one obtains plots regarding upcoming elections. By running
```
pipenv run python plot_history.py
```
one obtains plots containing data for past elections. The data for past elections is stored in the `data` folder. The output is stored in the `output` folder .

