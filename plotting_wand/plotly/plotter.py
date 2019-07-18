import plotly
import plotly.graph_objects as go


def plot(data=None, layout=None, **kwargs):
    # Get the API method
    api = kwargs.get('api', 'io.show')

    # Remove API from keyworded arguments
    kwargs.pop('api', None)

    # Build the figure data
    fig_data = {'data': data, 'layout': layout}

    # Create a Figure
    fig = go.Figure(fig_data)

    # Call the corresponding API method and return the corresponding graph
    # object
    if api == 'io.show':
        return io_show(fig, **kwargs)
    else:
        raise ValueError('Unsupported API "{}"'.format(api))


def io_show(fig, **kwargs):
    # Display the figure
    plotly.io.show(fig, **kwargs)

    # Return the figure
    return fig
