from Utils import arguments
from Cartesian import LineFromPoints

def print_output(output_line):
    if output_line is not None:
        print(f"The Corresponding Line is: ")
        print(f"{output_line}")


if __name__ == "__main__":
    args = arguments()
    input_one = args.input_one
    input_two = args.input_two
    output_line = LineFromPoints(
        input_one, input_two
        ).LineFormula()
    print_output(output_line)
