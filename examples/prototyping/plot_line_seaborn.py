from plotting_wand.plotter import plot, show

from examples.prototyping.data_processing import (
    read_file, process_data, build_data, build_layout)


def main():
    # Read the file contents
    df = read_file()

    # Process the data
    df = process_data(df)

    # Build the data
    data = build_data(df)

    # Build the layout
    layout = build_layout()

    # Plot the data
    plot(data=data, layout=layout, library='seaborn', kind='line')

    # Show the graph
    show()


if __name__ == '__main__':
    main()
