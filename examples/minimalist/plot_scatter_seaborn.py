from plotting_wand.plotter import plot, show

from examples.minimalist.data_processing import read_file, build_data


def main():
    # Read the file contents
    df = read_file()

    # Build the data
    data = build_data(df)

    # Plot the data
    plot(data=data, library='seaborn')

    # Show the graph
    show()


if __name__ == '__main__':
    main()
