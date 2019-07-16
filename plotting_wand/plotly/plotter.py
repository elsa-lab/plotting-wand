import plotly

from plotting_wand.plotly.data_processing import build_traces


def plot(data, **kwargs):
    # Get the API method
    api = kwargs.get('api', 'offline.plot')

    # Remove API from keyworded arguments
    kwargs.pop('api', None)

    # Build trace data
    data = build_traces(data)

    # Call the corresponding API method and return the corresponding graph
    # object
    if api == 'offline.plot':
        return offline_plot(data, **kwargs)
    elif api == 'offline.iplot':
        return offline_iplot(data, **kwargs)
    else:
        raise ValueError('Unsupported API "{}"'.format(api))


def offline_plot(data, **kwargs):
    return plotly.offline.plot(data, **kwargs)


def offline_iplot(data, **kwargs):
    return plotly.offline.iplot(data, **kwargs)
