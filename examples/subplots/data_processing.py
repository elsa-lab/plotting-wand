import datetime as dt
import pathlib

import pandas as pd

from plotting_wand.helpers.resampling import downsample
from plotting_wand.helpers.smoothing import smooth


# Set the column name to be used to specify which subplot
subplot_key = 'year'

# Set the column name for all X series
x_column_name = 'day_of_the_year'

# Set the column names for Y series in each subplot
# For example, the first series to be drawn is df['Phoenix']
y_column_names = ['Phoenix', 'Miami', 'Jerusalem', 'New York', 'Vancouver']


def read_file():
    # Set the relative path to the parent folder of this file
    relative_path = '../datasets/temperature.csv'

    # Build the full dataset path
    full_path = str(pathlib.Path(__file__).parent /
                    pathlib.Path(relative_path))

    # Read CSV file and return the contents
    return pd.read_csv(full_path)


def process_data(df):
    # Filter the data
    df = filter_data(df)

    # Convert the datetime to Pandas datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Add years to the data
    add_years_to_data(df)

    # Add days of the year to the data
    add_days_of_the_year_to_data(df)

    # Set the index as timestep
    df['t'] = df.index

    # Downsample the data
    df = downsample(df, 't', y_column_names, interval=100)

    # Smooth the data
    smooth_data(df)

    # Convert the temperature to Celsius
    convert_unit(df)

    # Return the processed dataframe
    return df


def filter_data(df):
    # Initialize the column names to keep
    keep = ['datetime']

    # Add column names for Y series
    keep.extend(y_column_names)

    # Keep only the selected columns
    filtered_df = df[keep]

    # Return a copy
    return filtered_df.copy()


def add_years_to_data(df):
    # Add years to the new column
    df[subplot_key] = df['datetime'].dt.year

    # Convert the years to string type
    df[subplot_key] = df[subplot_key].astype(str)


def add_days_of_the_year_to_data(df):
    # Add days of the year to the new column
    df[x_column_name] = df['datetime'].dt.dayofyear


def smooth_data(df):
    for column_name in y_column_names:
        # Get the temperature series
        temperatures = df[column_name]

        # Smooth the temperatures and save
        df[column_name] = smooth(temperatures, window=10)


def convert_unit(df):
    for column_name in y_column_names:
        # Get the temperature series
        temperatures = df[column_name]

        # Convert the temperatures to Celsius and save
        df[column_name] = temperatures - 273.15
