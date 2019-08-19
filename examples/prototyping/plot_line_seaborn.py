import pathlib

from plotting_wand.plotter import plot, save_image, show

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
    g = plot(data=data, layout=layout, library='seaborn', kind='line')

    # Get the image paths
    png_path = build_path('./images/plot_line_seaborn.py.png')
    pdf_path = build_path('./images/plot_line_seaborn.py.pdf')

    # Save the plotting result as image
    save_image(g, png_path)
    save_image(g, pdf_path)

    # Show the graph
    show()


def build_path(relative_path):
    # Build the path object
    path_obj = pathlib.Path(__file__).parent / pathlib.Path(relative_path)

    # Return the path
    return str(path_obj)


if __name__ == '__main__':
    main()
