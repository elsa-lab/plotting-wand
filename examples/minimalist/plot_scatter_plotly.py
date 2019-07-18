from plotting_wand.plotter import plot

from examples.minimalist.data_processing import read_file, build_data


def main():
    # Read the file contents
    contents = read_file()

    # Build the data
    data = build_data(contents)

    # Plot the data
    plot(data=data, renderer='browser')


if __name__ == '__main__':
    main()
