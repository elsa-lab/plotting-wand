import pathlib

from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


def read_file():
    # Set the relative path to the parent folder of this file
    dataset_path = '../datasets/temperature.csv'

    # Get the dataset path
    dataset_path = pathlib.Path(__file__).parent / pathlib.Path(dataset_path)

    # Read CSV file and return the contents
    return pd.read_csv(str(dataset_path))


def build_figure(contents):
    # Add index as timestep
    contents['t'] = contents.index

    # Downsample the data
    contents = downsample(contents, 't', interval=100)

    # Create the figure with predefined subplots
    fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
                        x_title='t', y_title=r'$^{\circ}C$')

    # Build the traces
    build_traces(contents, fig)

    # Update the layout
    update_layout(fig)

    # Return the figure
    return fig


def build_traces(contents, fig):
    # Set t as X data
    x = contents['t']

    # Set the column names to use for building traces in subplots
    column_names = [
        ['Vancouver', 'Los Angeles', 'Jerusalem'],  # Subplot 1
        ['San Francisco', 'Seattle', 'San Diego'],  # Subplot 2
        ['Las Vegas', 'Chicago', 'Detroit'],  # Subplot 3
    ]

    # Build trace for each subplot
    for col, column_names_per_subplot in enumerate(column_names):
        # Add all trace data to the current subplot
        for column_name in column_names_per_subplot:
            # Build the trace data for the current column name
            trace_data = build_trace_data(contents, x, column_name)

            # Add the trace data to the subplot
            fig.add_trace(trace_data, row=1, col=(col + 1))


def build_trace_data(contents, x, column_name):
    # Get the temperature series
    temperatures = contents[column_name]

    # Smooth the temperatures
    smoothed_temperatures = smooth(temperatures, window=10)

    # Convert the temperatures to Celsius
    temperatures_in_c = smoothed_temperatures - 273.15

    # Build the trace data
    trace_data = {
        'mode': 'lines',
        'name': column_name,
        'type': 'scattergl',  # See https://plot.ly/python/webgl-vs-svg/
        'x': x,
        'y': temperatures_in_c,
    }

    # Return the trace data
    return trace_data


def update_layout(fig):
    # Build the layout
    layout = {
        'title': {
            'text': 'City Temperatures',
        },
    }

    # Update the layout
    fig.update_layout(layout)
