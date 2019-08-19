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

    # Get the image paths
    png_path = build_path('./images/plot_line_plotly.py.png')
    pdf_path = build_path('./images/plot_line_plotly.py.pdf')

    # Save the figure as image
    save_image(fig, png_path)
    save_image(fig, pdf_path)


def build_path(relative_path):
    # Build the path object
    path_obj = pathlib.Path(__file__).parent / pathlib.Path(relative_path)

    # Return the path
    return str(path_obj)


if __name__ == '__main__':
    main()
