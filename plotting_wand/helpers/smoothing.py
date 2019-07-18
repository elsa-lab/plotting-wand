import pandas as pd


def smooth(data, window=1):
    """ Smooth the data.

    Arguments:
        data (pandas.DataFrame or pandas.Series): Data.
        window (int): Size of the moving window (greater than 0).

    Returns:
        pandas.Series: Smoothed data.
    """
    # Check the type of data
    if not isinstance(data, pd.DataFrame) and not isinstance(data, pd.Series):
        raise ValueError('"data" must be a pandas.DataFrame or pandas.Series')

    # Calculate rolling mean and return
    return data.rolling(window).mean()
