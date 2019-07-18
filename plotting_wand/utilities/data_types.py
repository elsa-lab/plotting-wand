def wrap_data_as_list(data):
    # Check the type of data
    if isinstance(data, dict):
        # Wrap the data with list and return
        return [data]
    elif isinstance(data, list):
        # Return the original list
        return data
    else:
        raise ValueError('Data must be a dict or list')
