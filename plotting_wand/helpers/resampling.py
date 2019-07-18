import numpy as np
import pandas as pd


def downsample(data, t_column, interval=1):
    """ Downsample the data.

    Arguments:
        data (pandas.DataFrame): Data.
        t_column (str): Timestep column.
        interval (number): Downsampling interval.
    """
    # Check the type of data
    if not isinstance(data, pd.DataFrame):
        raise ValueError('"data" must be a pandas.DataFrame')

    # Get timestep column
    t = data[t_column]

    # Build the resampling indexes
    resampling_indexes = np.floor(t / interval)

    # Group the data by the resampling indexes
    grouped_data = data.groupby(resampling_indexes)

    # Calculate the mean of the grouped data and return
    return grouped_data.mean()
