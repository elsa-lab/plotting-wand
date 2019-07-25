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


def build_path(image_path):
    # Build the image path
    image_path = pathlib.Path(__file__).parent / pathlib.Path(image_path)

    # Return the image path
    return str(image_path)


if __name__ == '__main__':
    main()
