import plotly
import plotly.graph_objects as go

from plotting_wand.utilities.attributes import nested_getattr


def plot(data=None, layout=None, **kwargs):
    # Get the API method
    api = kwargs.pop('api', 'io.show')

    # Get the API function
    fn = nested_getattr(plotly, api)

    # Get the figure
    figure = kwargs.pop('figure', None)

    # Build the figure object
    fig = build_figure_object(data, layout, figure)

    # Call the API function and return the figure object
    return call_plotting_function(fn, fig, **kwargs)


def save_image(fig, path, **kwargs):
    # Save the image
    fig.write_image(path, **kwargs)


def build_figure_object(data, layout, figure):
    # Check whether to use the figure
    if figure is None:
        # Build the figure data
        fig_data = {'data': data, 'layout': layout}
    else:
        # Use the figure directly
        fig_data = figure

    # Build a figure object and return
    return go.Figure(fig_data)


def call_plotting_function(fn, fig, **kwargs):
    # Call the function
    fn(fig, **kwargs)

    # Return the figure object
    return fig
