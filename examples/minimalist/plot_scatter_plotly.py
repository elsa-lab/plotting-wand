import pathlib

from plotting_wand.plotter import plot, save_image

from examples.minimalist.data_processing import read_file, build_data


def main():
    # Read the file contents
    df = read_file()

    # Build the data
    data = build_data(df)

    # Plot the data
    fig = plot(data=data, renderer='browser')

    # Get the image path
    image_path = build_image_path()

    # Save the plotting result as image
    save_image(fig, image_path)


def build_image_path():
    # Set the relative path to the parent folder of this file
    image_path = './plot_scatter_plotly.png'

    # Build the image path
    image_path = pathlib.Path(__file__).parent / pathlib.Path(image_path)

    # Return the image path
    return str(image_path)


if __name__ == '__main__':
    main()
