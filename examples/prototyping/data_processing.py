import pathlib

import pandas as pd

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


# Set the column names to use for building traces
y_column_names = ['Vancouver', 'Los Angeles', 'Jerusalem']


def read_file():
    # Set the relative path to the parent folder of this file
    relative_path = '../datasets/temperature.csv'

    # Build the full dataset path
    full_path = str(pathlib.Path(__file__).parent /
                    pathlib.Path(relative_path))

    # Read CSV file and return the contents
    return pd.read_csv(full_path)


def process_data(df):
    # Set the index as timestep
    df['t'] = df.index

    # Downsample the data
    df = downsample(df, 't', y_column_names, interval=100)

    # Process for each target column
    for y_column_name in y_column_names:
        # Get the temperature series
        temperatures = df[y_column_name]

        # Smooth the temperatures and save
        df[y_column_name] = smooth(temperatures, window=10)

        # Convert the temperatures to Celsius and save
        df[y_column_name] = temperatures - 273.15

    # Return processed data
    return df


def build_data(df):
    # Get the X series
    x = df['t']

    # Initialize the data
    data = []

    # Build trace data for each target column
    for y_column_name in y_column_names:
        # Get the Y series
        y = df[y_column_name]

        # Build the trace data
        trace_data = {
            'mode': 'lines',
            'name': y_column_name,
            'type': 'scatter',
            'x': x,
            'y': y,
        }

        # Add to the list
        data.append(trace_data)

    # Return the data
    return data


def build_layout():
    # Build the layout
    layout = {
        'title': {
            'text': 'City Temperatures',
        },
        'xaxis': {
            'title': {
                'text': 't',
            },
        },
        'yaxis': {
            'title': {
                'text': r'$^{\circ}C$',
            },
        },
    }

    # Return the layout
    return layout
