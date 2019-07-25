import pathlib

from plotting_wand.plotter import plot, save_image

from examples.minimalist.data_processing import read_file, build_data


def main():
    # Read the file contents
    df = read_file()

    # Build the data
    data = build_data(df)

    # Show the figure
    fig = plot(data=data, renderer='browser')

    # Get the image path
    image_path = build_path('./images/plot_scatter_plotly.py.png')

    # Save the figure as image
    save_image(fig, image_path)


def build_path(relative_path):
    # Build the path object
    path_obj = pathlib.Path(__file__).parent / pathlib.Path(relative_path)

    # Return the path
    return str(path_obj)


if __name__ == '__main__':
    main()
