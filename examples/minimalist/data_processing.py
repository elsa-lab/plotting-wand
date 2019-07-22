import pathlib

import pandas as pd


def read_file():
    # Set the relative path to the parent folder of this file
    dataset_path = '../datasets/insurance.csv'

    # Get the dataset path
    dataset_path = pathlib.Path(__file__).parent / pathlib.Path(dataset_path)

    # Read CSV file and return the contents
    return pd.read_csv(str(dataset_path))


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
