import pathlib

from plotting_wand.plotter import plot, save_image

from examples.subplots.data_processing import read_file, process_data
from examples.subplots.figure_building import build_figure


def main():
    # Read the file contents
    df = read_file()

    # Process the data
    df = process_data(df)

    # Build the figure
    fig = build_figure(df)

    # Show the figure
    fig = plot(figure=fig, renderer='browser')

    # Save the processed data
    df.to_csv(build_path('./processed_datasets/temperature.csv'))

    # Get the image paths
    png_path = build_path('./images/plot_line_plotly.py.png')
    eps_path = build_path('./images/plot_line_plotly.py.pdf')

    # Save the figure as images
    save_image(fig, png_path, width=900, height=300, scale=2)
    save_image(fig, eps_path, width=900, height=300, scale=2)


def build_path(image_path):
    # Build the image path
    image_path = pathlib.Path(__file__).parent / pathlib.Path(image_path)

    # Return the image path
    return str(image_path)


if __name__ == '__main__':
    main()
