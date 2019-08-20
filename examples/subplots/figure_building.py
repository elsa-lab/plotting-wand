from matplotlib.colors import to_hex
from plotly.subplots import make_subplots
import plotly.graph_objects as go

from plotting_wand.helpers.layout import adjust_annotations_font_sizes
from plotting_wand.helpers.layout import adjust_annotations_shifts
from plotting_wand.helpers.plotting import build_confidence_interval_traces

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
            # Get the column name for Y series
            y_column_name = y_column_names[trace_idx]

            # Get the trace color
            trace_color = trace_colors[trace_idx]

            # Build the legend name
            legend_name = build_legend_name(subplot_idx, y_column_name)

            # Build confidence interval traces
            trace_lo, trace_hi, trace_mean = build_confidence_interval_traces(
                df, x_column_name, y_column_name, legendgroup=y_column_name,
                line_color=trace_color, name=legend_name)

            # Only show the legend for the first subplot
            trace_mean.update(showlegend=(subplot_idx == 0))

            # Add confidence interval traces to the subplot
            fig.add_trace(trace_lo, row=1, col=(subplot_idx + 1))
            fig.add_trace(trace_hi, row=1, col=(subplot_idx + 1))

            # Add the trace data to the subplot
            fig.add_trace(trace_mean, row=1, col=(subplot_idx + 1))


def get_data_for_subplot(df_all, subplot_value):
    # Get the data matching the subplot value
    return df_all[df_all[subplot_key] == subplot_value]


def build_legend_name(subplot_idx, column_name):
    # Check whether it's the first subplot
    if subplot_idx == 0:
        return column_name
    else:
        return '{}({})'.format(column_name, subplot_idx)


def update_layout(fig):
    # Update the generic layout
    fig.update_layout(
        # Set the global font size
        font=dict(
            size=12
        ),
        # Set the legend attributes
        legend=dict(
            # Set the font size of the legend
            font=dict(size=12),
            # Set the position of the legend
            x=1.01,
            y=1.0,
            # Set the vertical space between legend groups
            tracegroupgap=0
        ),
        # Set the margins
        margin=dict(l=40, r=5, t=25, b=40)
    )

    # Update the X axis range
    fig.update_xaxes(range=[1, 365])

    # Adjust the font sizes of the annotations
    adjust_annotations_font_sizes(fig, factor=1.1)

    # Adjust distances from the axis labels to the subplots
    adjust_annotations_shifts(fig, x_factor=0.5, y_factor=0.5)
