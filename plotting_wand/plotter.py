import matplotlib.pyplot as plt

from plotting_wand.plotly.plotter import plot as plotly_plot
from plotting_wand.seaborn.plotter import plot as seaborn_plot


def plot(data, library='seaborn', **kwargs):
    # Wrap the data as list
    data = _wrap_data_as_list(data)

    # Call the corresponding plot function and return the corresponding graph
    # object
    if library == 'plotly':
        return plotly_plot(data, **kwargs)
    elif library == 'seaborn':
        return seaborn_plot(data, **kwargs)
    else:
        raise ValueError('Unknown library "{}"'.format(library))


def show():
    plt.show()


def _wrap_data_as_list(data):
    # Check the type of data
    if isinstance(data, dict):
        # Wrap the data with list and return
        return [data]
    elif isinstance(data, list):
        # Return the original list
        return data
    else:
        raise ValueError('Data must be a dict or list')
