import pathlib

import pandas as pd


def read_file():
    # Set the relative path to the parent folder of this file
    dataset_path = '../datasets/insurance.csv'

    # Get the dataset path
    dataset_path = pathlib.Path(__file__).parent / pathlib.Path(dataset_path)

    # Read CSV file and return the contents
    return pd.read_csv(str(dataset_path))


def build_plotting_data(file_data):
    # Set age as X data
    x = file_data['age']

    # Set charges price as Y data
    y = file_data['charges']

    # Build the plotting data
    data = {
        'type': 'scatter',
        'x': x,
        'y': y,
        'mode': 'markers',
    }

    # Return the plotting data
    return data
