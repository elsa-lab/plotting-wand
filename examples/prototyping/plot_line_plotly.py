import pathlib

from plotting_wand.plotter import plot, save_image

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

    # Show the figure
    fig = plot(data=data, layout=layout, renderer='browser')

    # Get the image path
    image_path = build_image_path('./images/plot_line_plotly.py.png')

    # Save the figure as image
    save_image(fig, image_path)


def build_image_path(image_path):
    # Build the image path
    image_path = pathlib.Path(__file__).parent / pathlib.Path(image_path)

    # Return the image path
    return str(image_path)


if __name__ == '__main__':
    main()
