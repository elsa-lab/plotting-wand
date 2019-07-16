import copy

import plotly.graph_objs as go


def build_traces(data):
    # Initialize the transformed traces
    transformed_traces = []

    # Iterate each trace data
    for trace_idx, trace_data in enumerate(data):
        # Initialize the new trace data
        new_trace_data = copy.deepcopy(trace_data)

        # Transform the trace data
        transform_trace_data(new_trace_data, trace_idx, trace_data)

        # Map the mode to the graph object
        GraphObj = map_graph_obj(new_trace_data)

        # Create a trace
        transformed_trace = GraphObj(**new_trace_data)

        # Add to the list
        transformed_traces.append(transformed_trace)

    # Return the transformed traces
    return transformed_traces


def transform_trace_data(new_trace_data, trace_idx, trace_data):
    update_mode(new_trace_data, trace_data)


def update_mode(new_trace_data, trace_data):
    # Get the mode of the trace data
    mode = trace_data.get('mode', 'markers')

    # Determine the new mode
    if mode == 'markers':
        new_mode = mode
    elif mode == 'lines':
        new_mode = mode
    elif mode == 'lines+lines':
        new_mode = mode
    elif mode == 'bar':
        new_mode = None
    else:
        raise ValueError('Unsupported graph object mode "{}"'.format(mode))

    # Set the new mode
    if new_mode is not None:
        new_trace_data['mode'] = new_mode


def map_graph_obj(trace_data):
    # Get the mode of the trace data
    mode = trace_data.get('mode', 'markers')

    if mode == 'markers':
        return go.Scatter
    elif mode == 'lines':
        return go.Scatter
    elif mode == 'lines+lines':
        return go.Scatter
    elif mode == 'bar':
        return go.Bar
    else:
        raise ValueError('Unsupported graph object mode "{}"'.format(mode))
