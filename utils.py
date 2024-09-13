def parse_cuts(cuts_input):
    """Parse a string of cuts into a list of tuples (width, height)."""
    try:
        return [(int(dim.split('x')[0]), int(dim.split('x')[1])) for dim in cuts_input.split(',')]
    except ValueError:
        raise ValueError("Invalid cuts input format. Expected format: widthxheight, widthxheight...")
