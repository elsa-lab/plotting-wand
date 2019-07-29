import pandas as pd


def smooth(data, apply_columns=None, window=1):
    """ Smooth the data.

    Arguments:
        data (pandas.DataFrame): Data.
        apply_columns (list of str): List of columns to apply smoothing. If the
            value is "None", all numeric series will be smoothed.
        window (int): Size of the moving window (greater than 0).

    Returns:
        pandas.Series: Smoothed data.
    """
    # Check the type of data
    if not isinstance(data, pd.DataFrame):
        raise ValueError('"data" must be a pandas.DataFrame')

    # Get numeric columns
    numeric_columns = set(data.select_dtypes(include='number'))

    # Set the columns to apply to all columns if it's None
    apply_columns = apply_columns or data.columns

    # Find the intersection with columns to apply
    apply_columns = numeric_columns & set(apply_columns)

    # Get numeric series
    numeric_df = data[apply_columns]

    # Calculate rolling mean
    smoothed_df = numeric_df.rolling(window).mean()

    # Get a copy of the data
    data = data.copy()

    # Update with smoothed series
    data.update(smoothed_df)

    # Return the updated data
    return data
