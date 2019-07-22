import copy

import pandas as pd

from plotting_wand.seaborn.logging import warn_unused_trace_data
from plotting_wand.utilities.attributes import deep_pop
from plotting_wand.utilities.data_types import convert_plotly_to_dict


def build_dataframe(data):
    # Initialize a list of transformed DataFrames
    transformed_dfs = []

    # Iterate each trace data
    for trace_idx, trace_data in enumerate(data):
        # Initialize the data for the DataFrame
        df_data = {}

        # Transform the trace data
        transform_trace_data(df_data, trace_idx, trace_data)

        # Build a new DataFrame
        df_trace = pd.DataFrame(data=df_data)

        # Add to the list
        transformed_dfs.append(df_trace)

    # Return the merged DataFrame
    return pd.concat(transformed_dfs)


def transform_trace_data(df_data, trace_idx, trace_data):
    # Convert trace data to dict
    trace_data = convert_plotly_to_dict(trace_data)

    # Clone the trace data
    trace_data = copy.deepcopy(trace_data)

    # Set various data
    set_x_and_y(df_data, trace_data)
    set_name(df_data, trace_idx, trace_data)

    # Warn about unused attributes
    warn_unused_trace_data(trace_idx, trace_data)


def set_x_and_y(df_data, trace_data):
    # Get the X and Y
    x = deep_pop(trace_data, 'x')
    y = deep_pop(trace_data, 'y')

    # Set the X and Y in the DataFrame data
    df_data.update({'x': x, 'y': y})


def set_name(df_data, trace_idx, trace_data):
    # Set the default trace name
    default_trace_name = '<Trace {}>'.format(trace_idx)

    # Get the name of the trace
    name = deep_pop(trace_data, 'name', default=default_trace_name)

    # Set the name in the DataFrame data
    df_data['name'] = name
