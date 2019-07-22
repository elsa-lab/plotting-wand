from plotting_wand.plotter import plot, show

from examples.subplots.data_processing import read_file, build_figure


def main():
    # Read the file contents
    df = read_file()

    # Build the figure
    fig = build_figure(df)

    # Plot the data
    plot(data=fig.data, layout=fig.layout, library='seaborn', kind='line')

    # Show the graph
    show()


if __name__ == '__main__':
    main()
