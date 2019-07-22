import datetime as dt
import pathlib

from matplotlib.colors import to_hex
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


# Set the date range for each subplot
date_ranges = [
    ['2014-01-01', '2014-12-31'],
    ['2015-01-01', '2015-12-31'],
    ['2016-01-01', '2016-12-31'],
]

# Set the numerical year
years = [
    2014,
    2015,
    2016,
]

# Set the subplot titles
subplot_titles = [
    'Year: 2014',
    'Year: 2015',
    'Year: 2016',
]

# Set the column names in each subplot
column_names = ['Phoenix', 'Miami', 'Jerusalem', 'New York', 'Vancouver']

# Set the colors for each trace
trace_colors = [
    to_hex('xkcd:red'),
    to_hex('xkcd:blue'),
    to_hex('xkcd:green'),
    to_hex('xkcd:orange'),
    to_hex('xkcd:gray'),
]


def read_file():
    # Set the relative path to the parent folder of this file
    dataset_path = '../datasets/temperature.csv'

    # Get the dataset path
    dataset_path = pathlib.Path(__file__).parent / pathlib.Path(dataset_path)

    # Read CSV file and return the contents
    return pd.read_csv(str(dataset_path))


def build_figure(df):
    # Process the contents
    df = process_contents(df)

    # Create the figure with predefined subplots
    fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
                        subplot_titles=subplot_titles,
                        x_title='Day of the Year', y_title=r'$^{\circ}C$')

    # Build the traces
    build_traces(df, fig)

    # Update the layout
    update_layout(fig)

    # Return the figure
    return fig


def process_contents(df):
    # Convert the datetime to Pandas datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Subtract the datetime with 1970/1/1 to get the timedelta
    timedelta = df['datetime'] - dt.datetime(1970, 1, 1)

    # Convert the timedelta to the epochs
    df['epoch'] = timedelta.dt.total_seconds()

    # Set the numerical year in the dataframe
    for date_range, year in zip(date_ranges, years):
        # Get the mask in the range
        filter_masks = (df['datetime'] >= date_range[0]) & (
            df['datetime'] < date_range[1])

        # Set the year in the original dataframe
        df.loc[filter_masks, 'year'] = year

    # Set the index as timestep
    df['t'] = df.index

    # Downsample the data
    df = downsample(df, 't', interval=100)

    # Return the processed dataframe
    return df


def build_traces(df, fig):
    # Build trace for each subplot
    for subplot_idx, year in enumerate(years):
        # Add the trace data to the current subplot
        for column_name, trace_color in zip(column_names, trace_colors):
            # Build the dataframe for the current subplot
            df_for_subplot = build_dataframe_for_subplot(df, year)

            # Build the trace data for the current column name
            trace_data = build_trace_data(
                df_for_subplot, subplot_idx, column_name, trace_color)

            # Add the trace data to the subplot
            fig.add_trace(trace_data, row=1, col=(subplot_idx + 1))


def build_dataframe_for_subplot(df, year):
    # Get the contents in the targeted year
    processed_df = df[df['year'] == year]

    # Get the epoch of the first row
    first_epoch = processed_df.iloc[0]['epoch']

    # Calculate the timedelta in seconds
    seconds = processed_df['epoch'] - first_epoch

    # Convert the seconds to days
    days = seconds / 86400

    # Get a copy of the processed dataframe to avoid SettingWithCopyWarning
    processed_df = processed_df.copy()

    # Set the days of the year
    processed_df['day'] = days + 1

    # Return the processed dataframe
    return processed_df


def build_trace_data(df, subplot_idx, column_name, trace_color):
    # Get the days as X
    x = df['day']

    # Get the temperature series
    temperatures = df[column_name]

    # Smooth the temperatures
    smoothed_temperatures = smooth(temperatures, window=10)

    # Convert the temperatures to Celsius
    y = smoothed_temperatures - 273.15

    # Build the trace data
    trace_data = {
        'line': {
            'color': trace_color,
        },
        'mode': 'lines',
        'name': column_name,
        # Only show the legend for the first subplot
        'showlegend': (subplot_idx == 0),
        'type': 'scatter',
        'x': x,
        'y': y,
    }

    # Return the trace data
    return trace_data


def update_layout(fig):
    # Build the layout data
    layout = {
        'title': {
            'text': 'City Temperatures',
        },
    }

    # Update the layout
    fig.update_layout(layout)

    # Update the X axis range
    fig.update_xaxes(range=[38.5, 365])
