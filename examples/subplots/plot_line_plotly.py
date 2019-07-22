from plotting_wand.plotter import plot

from examples.subplots.data_processing import read_file, build_figure


def main():
    # Read the file contents
    contents = read_file()

    # Build the figure
    fig = build_figure(contents)

    # Plot the data
    plot(figure=fig, renderer='browser')


if __name__ == '__main__':
    main()
