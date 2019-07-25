import pandas as pd


def smooth(data, apply_columns=None, window=1):
    """ Smooth the data.

    Arguments:
        data (pandas.DataFrame or pandas.Series): Data.
        apply_columns (list of str): List of columns to apply smoothing. If the
            value is "None", all numeric series will be smoothed.
        window (int): Size of the moving window (greater than 0).

    Returns:
        pandas.Series: Smoothed data.
    """
    # Check the type of data
    if not isinstance(data, pd.DataFrame) and not isinstance(data, pd.Series):
        raise ValueError('"data" must be a pandas.DataFrame or pandas.Series')

    # Get numeric columns
    numeric_columns = set(data.select_dtypes(include='number'))

    # Set the columns to apply to empty list if it's None
    apply_columns = apply_columns or []

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
