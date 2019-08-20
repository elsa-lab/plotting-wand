def reduce_annotations_shifts(fig, x_factor=1.0, y_factor=1.0):
    """ Reduce annotation shifts.

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
