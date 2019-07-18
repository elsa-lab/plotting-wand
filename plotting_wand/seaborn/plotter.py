import seaborn as sns

from plotting_wand.seaborn.data_processing import merge_data_into_df


def plot(data=None, layout=None, **kwargs):
    # Get the API method
    api = kwargs.get('api', 'relplot')

    # Remove API from keyworded arguments
    kwargs.pop('api', None)

    # Merge data into a DataFrame
    data = merge_data_into_df(data)

    # Call the corresponding API method and return the corresponding graph
    # object
    if api == 'relplot':
        return relplot(data, **kwargs)
    else:
        raise ValueError('Unsupported API "{}"'.format(api))


def relplot(data, **kwargs):
    return sns.relplot(x='x', y='y', hue='name', data=data, **kwargs)
