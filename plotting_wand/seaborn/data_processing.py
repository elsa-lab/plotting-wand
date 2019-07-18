import pandas as pd


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
    set_x_and_y(df_data, trace_data)
    set_name(df_data, trace_idx, trace_data)


def set_name(df_data, trace_idx, trace_data):
    # Set the default trace name
    default_trace_name = '<Trace {}>'.format(trace_idx)

    # Get the name of the trace
    name = trace_data.get('name', default_trace_name)

    # Set the name in the DataFrame data
    df_data['name'] = name


def set_x_and_y(df_data, trace_data):
    # Get the X and Y
    x = trace_data.get('x', None)
    y = trace_data.get('y', None)

    # Set the X and Y in the DataFrame data
    df_data.update({'x': x, 'y': y})
