import seaborn as sns

from plotting_wand.seaborn.data_processing import build_dataframe


def plot(data=None, layout=None, **kwargs):
    # Get the API method
    api = kwargs.pop('api', 'relplot')

    # Build a dataframe
    data = build_dataframe(data)

    # Call the corresponding API function and return the corresponding graph
    # object
    if api == 'relplot':
        return relplot(data, **kwargs)
    else:
        raise ValueError('Unsupported API function "{}"'.format(api))


def relplot(data, **kwargs):
    return sns.relplot(x='x', y='y', hue='name', data=data, **kwargs)
