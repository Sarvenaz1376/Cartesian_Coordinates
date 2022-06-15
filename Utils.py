import argparse

def arguments():
    """
    parses the inputs arguments
    """
    parser = argparse.ArgumentParser(description="Parses the input arguments")
    parser.add_argument(
        "-o",
        "--input_one",
        nargs=2,
        type=int,
        help="Could be either int or float",
    )
    parser.add_argument(
        "-t",
        "--input_two",
        nargs=2,
        type=int,
        help="Could be either int or float",
    )
    return parser.parse_args()

