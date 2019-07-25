def reduce_annotations_shifts(fig, factor=1.0):
    """ Reduce annotation shifts.

    Arguments:
        fig (plotly.graph_objs._figure.Figure): Plotly figure.
        factor (float): The shifts are multiplied with this factor.
    """
    # Set the attributes to reduce
    attrs = ['xshift', 'yshift']

    # Get the annotation object
    annotations = getattr(fig.layout, 'annotations', [])

    # Update each annotation
    for annotation in annotations:
        # Reduce spacing for each attribute
        for attr in attrs:
            # Check whether the value exists
            if getattr(annotation, attr, None) is not None:
                # Multiply the attribute by the factor
                annotation[attr] *= factor
