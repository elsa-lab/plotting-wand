from plotting_wand.plotter import plot

from examples.subplots.data_processing import read_file, process_data
from examples.subplots.figure_building import build_figure


def main():
    # Read the file contents
    df = read_file()

    # Process the data
    df = process_data(df)

    # Build the figure
    fig = build_figure(df)

    # Plot the data
    plot(figure=fig, renderer='browser')


if __name__ == '__main__':
    main()
