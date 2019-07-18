import functools


def nested_getattr(obj, attr, *args):
    """ Nested getattr.
    """
    """ Reference: https://stackoverflow.com/a/31174427
    """
    def _getattr(obj, attr):
        return getattr(obj, attr, *args)

    return functools.reduce(_getattr, [obj] + attr.split('.'))
