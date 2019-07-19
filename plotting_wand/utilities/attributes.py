import functools


def nested_getattr(obj, attr, *args):
    """ Nested getattr.
    """
    """ Reference: https://stackoverflow.com/a/31174427
    """
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split('.'))


def deep_pop(obj, path, default=None):
    # Split the attribute path
    attrs = path.split('.')

    # Initialize the parent object records
    objects = []

    # Go to the deepest nested object
    for attr in attrs[:-1]:
        # Add the parent object to the records
        objects.append(obj)

        try:
            # Try to access the child object
            obj = obj[attr]
        except:
            # Return the default value
            return default

    # Get the last attribute
    last_attr = attrs[-1]

    # Pop the attribute
    value = obj.pop(last_attr, default)

    # Add the last object to the records
    objects.append(obj)

    # Pop the empty parent objects
    for idx in range(len(objects) - 2, -1, -1):
        # Get the parent and child objects
        parent = objects[idx]
        child = objects[idx + 1]

        # Get the child key
        child_key = attrs[idx]

        # Check whether the child object is empty
        if len(child) <= 0:
            parent.pop(child_key, None)

    # Return the popped value
    return value
