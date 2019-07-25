import numpy as np
import pandas as pd
import plotly.graph_objects as go
import scipy.stats as st


def build_confidence_interval_traces(
        data, x_column, y_column, ci=0.95, **kwargs):
    """ Build confidence interval area traces.

    Confidence interval is calculated among same timestep but different
    categories.

    References:
    https://stackoverflow.com/questions/15033511/compute-a-confidence-interval-from-sample-data
    https://kite.com/python/examples/702/scipy-compute-a-confidence-interval-from-a-dataset

    Arguments:
        data (pandas.DataFrame) Data.
        x_column (str): X series column.
        y_column (str): Y series column.
        ci (float): Confidence interval.
        kwargs: Arguments passed to "fig.add_trace" function.

    Returns:
        [trace_lo, trace_hi, trace_mean]:
            trace_lo: Trace of lower bounds.
            trace_hi: Trace of higher bounds.
            trace_mean: Trace of mean values.
    """
    # Check the type of data
    if not isinstance(data, pd.DataFrame):
        raise ValueError('"data" must be a pandas.DataFrame')

    # Group the data by X column
    grouped_by_x = data.groupby(x_column)

    # Get the number of groups
    num_groups = len(grouped_by_x)

    # Initialize the X series
    xs = np.zeros(num_groups)

    # Initialize the Y series of lower bounds, upper bounds and mean values
    y_lo, y_hi, y_mean = np.zeros(num_groups), np.zeros(
        num_groups), np.zeros(num_groups)

    # Add confidence interval at each X
    for idx, (x, group) in enumerate(grouped_by_x):
        # Get the Y series
        y = group[y_column]

        # Calculate bounds of confidence interval
        num = len(y)
        mean_s = np.mean(y)
        std_err = st.sem(y)
        h = std_err * st.t.ppf((1 + ci) / 2, num - 1)
        lo, hi = mean_s - h, mean_s + h

        # Add X to the list
        xs[idx] = x

        # Add bounds to the lists
        y_lo[idx] = lo
        y_hi[idx] = hi

        # Add mean values to the list
        y_mean[idx] = mean_s

    # Set common attributes for building traces for confidence interval
    ci_attrs = dict(hoverinfo='skip', line_width=0,
                    mode='lines', showlegend=False)

    # Build the lower bounds line
    trace_lo = go.Scatter(x=xs, y=y_lo, fill=None, **ci_attrs, **kwargs)

    # Build the upper bounds line which fills the area between this one and
    # lower bounds line
    trace_hi = go.Scatter(x=xs, y=y_hi, fill='tonexty', **ci_attrs, **kwargs)

    # Build the mean values line
    trace_mean = go.Scatter(x=xs, y=y_mean, mode='lines', **kwargs)

    # Return the lower bound, upper bounds and mean values traces
    return [trace_lo, trace_hi, trace_mean]
