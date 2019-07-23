import os
import pathlib

import matplotlib.pyplot as plt

from plotting_wand.plotly.plotter import plot as plotly_plot
from plotting_wand.plotly.plotter import save_image as plotly_save_image
from plotting_wand.seaborn.plotter import plot as seaborn_plot
from plotting_wand.seaborn.plotter import save_image as seaborn_save_image


def plot(data=None, layout=None, library='plotly', **kwargs):
    """ Plot the data.

    Arguments:
        data: Plotting data.
        layout: Layout data.
        library (str): Plotting library to use.

    Returns:
        Corresponding graph object.
    """

    # Call the corresponding plot function and return the corresponding graph
    # object
    if library == 'plotly':
        return plotly_plot(data=data, layout=layout, **kwargs)
    elif library == 'seaborn':
        return seaborn_plot(data=data, layout=layout, **kwargs)
    else:
        raise ValueError('Unknown library "{}"'.format(library))


def save_image(fig, path, **kwargs):
    """ Save the plotting result as an image.

    Arguments:
        fig: Figure object returned from the function "plot".
        path (str): Path to save.
    """
    # Create the directory if it doesn't exist
    parent_dir_obj = pathlib.Path(path).parent
    parent_dir_obj.mkdir(parents=True, exist_ok=True)

    # Check the figure object type and call the corresponding saving function
    if hasattr(fig, 'write_image'):
        plotly_save_image(fig, path, **kwargs)
    elif hasattr(fig, 'savefig'):
        seaborn_save_image(fig, path, **kwargs)
    else:
        raise ValueError('Unknown figure object type')


def show():
    """ Show the graph.

    You should use it only when plotting with Seaborn and a Python file.
    """
    plt.show()
