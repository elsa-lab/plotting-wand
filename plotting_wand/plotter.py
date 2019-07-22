import matplotlib.pyplot as plt

from plotting_wand.plotly.plotter import plot as plotly_plot
from plotting_wand.seaborn.plotter import plot as seaborn_plot


def plot(data=None, layout=None, library='plotly', **kwargs):
    # Call the corresponding plot function and return the corresponding graph
    # object
    if library == 'plotly':
        return plotly_plot(data=data, layout=layout, **kwargs)
    elif library == 'seaborn':
        return seaborn_plot(data=data, layout=layout, **kwargs)
    else:
        raise ValueError('Unknown library "{}"'.format(library))


def show():
    plt.show()
