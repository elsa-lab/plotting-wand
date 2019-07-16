import pandas as pd

from plotting_wand.plotter import plot, show


def read_file():
    return pd.read_csv('examples/datasets/insurance.csv')


def build_plotting_data(file_data):
    # Set age as X data
    x = file_data['age']

    # Set charges price as Y data
    y = file_data['charges']

    # Build the plotting data
    data = {
        'x': x,
        'y': y,
    }

    # Return the plotting data
    return data


def main():
    # Read the file data
    file_data = read_file()

    # Build the plotting data
    plotting_data = build_plotting_data(file_data)

    # Plot the data
    plot(plotting_data, library='seaborn')

    # Show the graph
    show()


if __name__ == '__main__':
    main()
