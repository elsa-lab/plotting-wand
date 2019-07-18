from plotting_wand.plotter import plot, show

from examples.minimalist.data_processing import read_file, build_plotting_data


def main():
    # Read the file data
    file_data = read_file()

    # Build the plotting data
    plotting_data = build_plotting_data(file_data)

    # Plot the data
    plot(data=plotting_data)

    # Show the graph
    show()


if __name__ == '__main__':
    main()
