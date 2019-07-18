import pathlib

import pandas as pd

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


def read_file():
    # Set the relative path to the parent folder of this file
    dataset_path = '../datasets/temperature.csv'

    # Get the dataset path
    dataset_path = pathlib.Path(__file__).parent / pathlib.Path(dataset_path)

    # Read CSV file and return the contents
    return pd.read_csv(str(dataset_path))


def build_data(contents):
    # Add index as timestep
    contents['t'] = contents.index

    # Downsample the data
    contents = downsample(contents, 't', interval=100)

    # Set t as X data
    x = contents['t']

    # Set the column names to use for building traces
    column_names = ['Vancouver', 'Los Angeles', 'Jerusalem']

    # Initialize the data
    data = []

    # Iterate each column name
    for column_name in column_names:
        # Get the temperature series
        temperatures = contents[column_name]

        # Smooth the temperatures
        smoothed_temperatures = smooth(temperatures, window=10)

        # Convert the temperature to Celsius
        temperature_in_c = smoothed_temperatures - 273.15

        # Build the trace data
        trace_data = {
            'mode': 'lines',
            'name': column_name,
            'type': 'scattergl',  # See https://plot.ly/python/webgl-vs-svg/
            'x': x,
            'y': temperature_in_c,
        }

        # Add to the list
        data.append(trace_data)

    # Return the data
    return data


def build_layout():
    # Build the layout
    layout = {}

    # Return the layout
    return layout
