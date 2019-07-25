import numpy as np
import pandas as pd


def downsample(data, t_column, category_columns=[], interval=1):
    """ Downsample the data.

    The downsampling consists of the following steps:
    1. Build the resampling indexes by dividing the timestep column values by
    the interval and converted to floor values
    2. The data are grouped by the resampling indexes and category columns
    3. Numeric data are aggregated by mean function
    4. Non-numeric data are aggregated by taking the first row in each group

    Arguments:
        data (pandas.DataFrame): Data.
        t_column (str): Timestep column.
        category_columns (list of str): List of columns to be treated as
            categories. Downsampling will only apply on the data in the same
            category.
        interval (number): Downsampling interval.
    """
    # Define the first row extraction function
    def first_row(s):
        return s.iloc[0]

    # Check the type of data
    if not isinstance(data, pd.DataFrame):
        raise ValueError('"data" must be a pandas.DataFrame')

    # Get a copy of the data
    data = data.copy()

    # Get timestep column
    t = data[t_column]

    # Build the resampling indexes
    resampling_indexes = np.floor(t / interval)

    # Add resampling indexes to the data
    data['_resampling_indexes'] = resampling_indexes

    # Build the grouping columns
    grouping_columns = ['_resampling_indexes', *category_columns]

    # Group the data by the grouping columns
    grouped_data = data.groupby(grouping_columns, as_index=False)

    # Get the columns to be applied
    numeric_columns = data.select_dtypes(include='number')
    non_numeric_columns = data.select_dtypes(exclude='number')

    # Build the aggregation mapping
    mean_agg_map = {name: 'mean' for name in numeric_columns}
    first_row_agg_map = {name: first_row for name in non_numeric_columns}

    # Combine the aggregation mappings
    agg_map = {**mean_agg_map, **first_row_agg_map}

    # Remove resampling indexes column from aggregation mappings
    agg_map.pop('_resampling_indexes', None)

    # Remove category column from aggregation mappings
    [agg_map.pop(c, None) for c in category_columns]

    # Aggregate the grouped data
    aggregated = grouped_data.aggregate(agg_map)

    # Drop the resampling indexes column and return
    return aggregated.drop(columns='_resampling_indexes')
