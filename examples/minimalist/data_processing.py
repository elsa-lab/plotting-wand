import pandas as pd


def read_file():
    return pd.read_csv('examples/datasets/insurance.csv')


def build_plotting_data(file_data):
    # Set age as X data
    x = file_data['age']

    # Set charges price as Y data
    y = file_data['charges']

    # Build the plotting data
    data = {
        'type': 'scatter',
        'x': x,
        'y': y,
        'mode': 'markers',
    }

    # Return the plotting data
    return data
