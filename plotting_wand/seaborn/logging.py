import json

from plotting_wand.utilities.logging import warn


def warn_unused_trace_data(trace_idx, trace_data):
    # Skip the warning if the data is none or empty
    if trace_data is None or len(trace_data) <= 0:
        return

    # Convert the trace data to JSON
    trace_data_as_json = json.dumps(trace_data)

    # Warn about the unused attributes
    warn('Warning: Unused attributes in trace data [{}]: {}'.format(
        trace_idx, trace_data_as_json))


def warn_unused_layout(layout):
    # Skip the warning if the data is none or empty
    if layout is None or len(layout) <= 0:
        return

    # Convert the layout to JSON
    layout_as_json = json.dumps(layout)

    # Warn about the unused attributes
    warn('Warning: Unused attributes in layout: {}'.format(layout_as_json))
