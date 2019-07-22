from plotting_wand.plotter import plot

from examples.prototyping.data_processing import (
    read_file, build_data, build_layout)


def main():
    # Read the file contents
    df = read_file()

    # Build the data
    data = build_data(df)

    # Build the layout
    layout = build_layout()

    # Plot the data
    plot(data=data, layout=layout, renderer='browser')


if __name__ == '__main__':
    main()
