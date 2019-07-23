import numpy as np
import pandas as pd


def downsample(data, t_column, apply_columns, interval=1):
    """ Downsample the data.

    The downsampling consists of the following steps:
    1. Build the resampling indexes by dividing the timestep column values by
    the interval and converted to floor values
    2. The data are grouped by the resampling indexes
    3. Columns to be applied are aggregated by mean function
    4. Other columns are aggregated by median index function

    Arguments:
        data (pandas.DataFrame): Data.
        t_column (str): Timestep column.
        apply_columns (list of str): List of columns to apply downsampling.
        interval (number): Downsampling interval.
    """
    # Define the median index function
    def median_index(s):
        return s.iloc[len(s) // 2]

    # Check the type of data
    if not isinstance(data, pd.DataFrame):
        raise ValueError('"data" must be a pandas.DataFrame')

    # Get timestep column
    t = data[t_column]

    # Build the resampling indexes
    resampling_indexes = np.floor(t / interval)

    # Group the data by the resampling indexes
    grouped_data = data.groupby(resampling_indexes)

    # Get all columns
    all_columns = set(data.columns)

    # Get the columns to be applied with median index function
    other_columns = all_columns - set(apply_columns)

    # Build the aggregation mapping
    mean_agg_map = {name: 'mean' for name in apply_columns}
    median_index_agg_map = {name: median_index for name in other_columns}

    # Combine the aggregation mappings
    agg_map = {**mean_agg_map, **median_index_agg_map}

    # Aggregate the grouped data and return
    return grouped_data.agg(agg_map)
