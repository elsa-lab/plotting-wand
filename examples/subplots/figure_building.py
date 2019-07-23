from matplotlib.colors import to_hex
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from examples.subplots.data_processing import (
    subplot_key, x_column_name, y_column_names)


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

# Set the colors for each trace
# See https://xkcd.com/color/rgb/ for the color names
trace_colors = [
    to_hex('xkcd:red'),
    to_hex('xkcd:blue'),
    to_hex('xkcd:green'),
    to_hex('xkcd:orange'),
    to_hex('xkcd:gray'),
]


def build_figure(df):
    # Create the figure with predefined subplots
    fig = make_subplots(rows=1, cols=3, shared_yaxes=True,
                        horizontal_spacing=0.04, vertical_spacing=0.06,
                        subplot_titles=subplot_titles,
                        x_title='Day of the Year', y_title=r'$^{\circ}C$')

    # Build the traces
    build_traces(df, fig)

    # Update the layout
    update_layout(fig)

    # Return the figure
    return fig


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


def get_data_for_subplot(df_all, subplot_value):
    # Get the data matching the subplot value
    return df_all[df_all[subplot_key] == subplot_value]


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
    # Update the generic layout
    fig.update_layout(
        legend=dict(x=1.01, y=1.0),
        margin=dict(l=5, r=5, t=25, b=5)
    )

    # Update the X axis range
    fig.update_xaxes(range=[38.5, 365])
