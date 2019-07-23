import datetime as dt
import pathlib

from matplotlib.colors import to_hex
from plotly.subplots import make_subplots
import pandas as pd
import plotly.graph_objects as go

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


# Set the column name to be used to specify which subplot
subplot_key = 'year'

# Set the target value of each subplot
# For example, if df[subplot_key] == '2014', df[df[subplot_key] == '2014'] will
# be drawn into the first subplot
subplot_values = [
    '2014',
    '2015',
    '2016',
]

# Set the subplot titles
subplot_titles = [
    'Year: 2014',
    'Year: 2015',
    'Year: 2016',
]

# Set the column name for all X series
x_column_name = 'day_of_the_year'

# Set the column names for Y series in each subplot
# For example, the first series to be drawn is df['Phoenix']
y_column_names = ['Phoenix', 'Miami', 'Jerusalem', 'New York', 'Vancouver']

# Set the colors for each trace
# See https://xkcd.com/color/rgb/ for the color names
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
    # Process the data
    df = process_data(df)

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


def process_data(df):
    # Filter the data
    df = filter_data(df)

    # Convert the datetime to Pandas datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Add years to the data
    add_years_to_data(df)

    # Add days of the year to the data
    add_days_of_the_year_to_data(df)

    # Set the index as timestep
    df['t'] = df.index

    # Downsample the data
    df = downsample(df, 't', y_column_names, interval=100)

    # Smooth the data
    smooth_data(df)

    # Convert the temperature to Celsius
    convert_unit(df)

    # Return the processed dataframe
    return df


def filter_data(df):
    # Initialize the column names to keep
    keep = ['datetime']

    # Add column names for Y series
    keep.extend(y_column_names)

    # Keep only the selected columns
    filtered_df = df[keep]

    # Return a copy
    return filtered_df.copy()


def add_years_to_data(df):
    # Add years to the new column
    df['year'] = df['datetime'].dt.year

    # Convert the years to string type
    df['year'] = df['year'].astype(str)


def add_days_of_the_year_to_data(df):
    # Add days of the year to the new column
    df['day_of_the_year'] = df['datetime'].dt.dayofyear


def smooth_data(df):
    for column_name in y_column_names:
        # Get the temperature series
        temperatures = df[column_name]

        # Smooth the temperatures and save
        df[column_name] = smooth(temperatures, window=10)


def convert_unit(df):
    for column_name in y_column_names:
        # Get the temperature series
        temperatures = df[column_name]

        # Convert the temperatures to Celsius and save
        df[column_name] = temperatures - 273.15


def get_data_for_subplot(df_all, subplot_value):
    # Get the data matching the subplot value
    return df_all[df_all[subplot_key] == subplot_value]


def build_traces(df_all, fig):
    # Build traces for each subplot
    for subplot_idx, subplot_value in enumerate(subplot_values):
        # Get the data for the current subplot
        df = get_data_for_subplot(df_all, subplot_value)

        # Add trace for each column name
        for trace_idx in range(len(y_column_names)):
            # Build the trace data
            trace_data = build_trace_data(df, subplot_idx, trace_idx)

            # Add the trace data to the subplot
            fig.add_trace(trace_data, row=1, col=(subplot_idx + 1))


def build_trace_data(df, subplot_idx, trace_idx):
    # Get the column name for Y series
    y_column_name = y_column_names[trace_idx]

    # Get the trace color
    trace_color = trace_colors[trace_idx]

    # Get the X series
    x = df[x_column_name]

    # Get the Y series
    y = df[y_column_name]

    # Build the trace data
    trace_data = {
        'line': {
            'color': trace_color,
        },
        'mode': 'lines',
        'name': y_column_name,
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
