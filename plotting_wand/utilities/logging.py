import sys


def warn(message, **kwargs):
    print(message, file=sys.stderr, **kwargs)
