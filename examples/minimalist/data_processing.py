import pathlib

import pandas as pd


def read_file():
    # Set the relative path to the parent folder of this file
    relative_path = '../datasets/insurance.csv'

    # Build the full dataset path
    full_path = str(pathlib.Path(__file__).parent /
                    pathlib.Path(relative_path))

    # Read CSV file and return the contents
    return pd.read_csv(full_path)


def build_data(df):
    # Set age as X data
    x = df['age']

    # Set charges price as Y data
    y = df['charges']

    # Build the data
    data = {
        'type': 'scatter',
        'x': x,
        'y': y,
        'mode': 'markers',
    }

    # Return the data
    return data
