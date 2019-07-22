def wrap_data_as_list(data):
    # Check the type of data
    if isinstance(data, list):
        # Return the original list
        return data
    elif isinstance(data, tuple):
        # Convert the tuple to the list and return
        return list(data)
    elif isinstance(data, dict):
        # Wrap the data with list and return
        return [data]
    else:
        raise ValueError('Data must be a list, tuple or dict')
