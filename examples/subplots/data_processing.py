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

    # Fill NaNs by interpolation
    df = df.interpolate(limit_direction='both')

    # Convert the datetime to Pandas datetime
    df['datetime'] = pd.to_datetime(df['datetime'])

    # Add years to the data
    add_years_to_data(df)

    # Add days of the year to the data
    add_days_of_the_year_to_data(df)

    # Add hours to the data
    add_hours_to_data(df)

    # Split data by hour
    dfs = split_by_hour(df)

    # Downsample the data
    dfs = downsample_data(dfs)

    # Smooth the data
    smooth_data(dfs)

    # Merge dataframes
    df = pd.concat(dfs)

    # Convert the temperature to Celsius
    convert_unit(df)

    # Clean the data (Optional)
    df = clean_data(df)

    # Return the processed dataframe
    return df


def filter_data(df):
    # Initialize the column names to keep
    keep = ['datetime']

    # Add column names for Y series
    keep.extend(y_column_names)

    # Keep only the selected columns and return
    return df[keep]


def add_years_to_data(df):
    # Add years to the new column
    df[subplot_key] = df['datetime'].dt.year

    # Convert the years to string type
    df[subplot_key] = df[subplot_key].astype(str)


def add_days_of_the_year_to_data(df):
    # Add days of the year to the new column
    df[x_column_name] = df['datetime'].dt.dayofyear


def add_hours_to_data(df):
    # Add hours to the new column
    df['hour'] = df['datetime'].dt.hour


def split_by_hour(df):
    # Group by hour
    grouped = df.groupby('hour')

    # Build each splitted dataframe and return
    return [group for _, group in grouped]


def downsample_data(dfs):
    # Downsample the data by day of the year and return
    return [downsample(df, x_column_name,
                       category_columns=[subplot_key], interval=2)
            for df in dfs]


def smooth_data(dfs):
    for df in dfs:
        # Split the series by year
        grouped_by_year = df.groupby(subplot_key)

        # Smooth each group
        smoothed = [smooth(group, apply_columns=y_column_names, window=10)
                    for _, group in grouped_by_year]

        # Merge all smoothed series
        merged = pd.concat(smoothed)

        # Update the temperature series
        df.update(merged)


def convert_unit(df):
    for column_name in y_column_names:
        # Get the temperature series
        temperatures = df[column_name]

        # Convert the temperatures to Celsius and save
        df[column_name] = temperatures - 273.15


def clean_data(df):
    # Reorder the columns
    df = df[['datetime', 'year', 'day_of_the_year', 'hour', *y_column_names]]

    # Sort the values by datetime
    df = df.sort_values(by=['year', 'day_of_the_year', 'hour'])

    # Reset the index and return
    return df.reset_index(drop=True)
