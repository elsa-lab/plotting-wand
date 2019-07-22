import copy

from plotting_wand.seaborn.logging import warn_unused_layout
from plotting_wand.utilities.attributes import deep_pop
from plotting_wand.utilities.data_types import convert_plotly_to_dict


def set_layout(g, layout):
    # Convert the layout to dict
    layout = convert_plotly_to_dict(layout)

    # Clone the layout
    layout = copy.deepcopy(layout)

    # Set various layout attributes
    set_title(g, layout)
    set_axes_labels(g, layout)

    # Warn about unused attributes
    warn_unused_layout(layout)


def set_title(g, layout):
    # Get the title
    title = deep_pop(layout, 'title.text')

    # Set the title
    g.ax.set_title(title)


def set_axes_labels(g, layout):
    # Get the titles
    x_axis_title = deep_pop(layout, 'xaxis.title.text')
    y_axis_title = deep_pop(layout, 'yaxis.title.text')

    # Set the axes labels
    g.ax.set_xlabel(x_axis_title)
    g.ax.set_ylabel(y_axis_title)
