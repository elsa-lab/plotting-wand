import pathlib

from plotting_wand.plotter import plot, save_image, show

from examples.minimalist.data_processing import read_file, build_data


def main():
    # Read the file contents
    df = read_file()

    # Build the data
    data = build_data(df)

    # Plot the data
    g = plot(data=data, library='seaborn')

    # Get the image path
    image_path = build_path('./images/plot_scatter_seaborn.py.png')

    # Save the plotting result as image
    save_image(g, image_path)

    # Show the graph
    show()


def build_path(relative_path):
    # Build the path object
    path_obj = pathlib.Path(__file__).parent / pathlib.Path(relative_path)

    # Return the path
    return str(path_obj)


if __name__ == '__main__':
    main()
