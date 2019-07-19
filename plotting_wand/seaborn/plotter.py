import seaborn as sns

from plotting_wand.seaborn.data_processing import build_dataframe
from plotting_wand.seaborn.post_processing import set_layout


def plot(data=None, layout=None, **kwargs):
    # Get the API method
    api = kwargs.pop('api', 'relplot')

    # Build a dataframe
    data = build_dataframe(data)

    # Call the corresponding API function
    if api == 'relplot':
        g = relplot(data, **kwargs)
    else:
        raise ValueError('Unsupported API function "{}"'.format(api))

    # Set the layout
    set_layout(g, layout)

    # Return the corresponding Seaborn object
    return g


def relplot(data, **kwargs):
    return sns.relplot(x='x', y='y', hue='name', data=data, **kwargs)
