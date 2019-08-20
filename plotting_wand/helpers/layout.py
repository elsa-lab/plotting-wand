def adjust_annotations_font_sizes(fig, factor=1.0):
    """ Adjust annotation font sizes.

    Arguments:
        fig (plotly.graph_objs._figure.Figure): Plotly figure.
        factor (float): The font sizes are multiplied with this factor.
    """
    # Get the annotation object
    annotations = getattr(fig.layout, 'annotations', [])

    # Update each annotation
    for annotation in annotations:
        # Get the font
        font = getattr(annotation, 'font', None)

        # Check whether the font attribute exists
        if font is not None:
            # Get the size
            size = getattr(font, 'size', None)

            # Check whether the size attribute exists
            if size is not None:
                # Multiply the attribute by the factor
                font['size'] *= factor


def adjust_annotations_shifts(fig, x_factor=1.0, y_factor=1.0):
    """ Adjust annotation shifts.

    Arguments:
        fig (plotly.graph_objs._figure.Figure): Plotly figure.
        x_factor (float): The X shifts are multiplied with this factor.
        y_factor (float): The Y shifts are multiplied with this factor.
    """
    # Set the attributes to reduce
    attrs = ['xshift', 'yshift']

    # Set the corresponding factors
    factors = [x_factor, y_factor]

    # Get the annotation object
    annotations = getattr(fig.layout, 'annotations', [])

    # Update each annotation
    for annotation in annotations:
        # Reduce spacing for each attribute
        for attr, factor in zip(attrs, factors):
            # Check whether the value exists
            if getattr(annotation, attr, None) is not None:
                # Multiply the attribute by the factor
                annotation[attr] *= factor
