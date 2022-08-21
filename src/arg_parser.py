# This is the main code of this project nr, and it manages running the code and
# outputting the results to LaTex.
import argparse


def parse_cli_args():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description="Optional app description")

    ## Include argument parsing for data exporting code.
    # Compile LaTex
    parser.add_argument(
        "--l", action="store_true", help="Boolean indicating if code compiles LaTex"
    )

    # Generate, compile and export Dynamic PlantUML diagrams to LaTex.
    parser.add_argument(
        "--dd",
        action="store_true",
        help="A boolean indicating if code generated diagrams are compiled and exported.",
    )
    # Generate, compile and export Static PlantUML diagrams to LaTex.
    parser.add_argument(
        "--sd",
        action="store_true",
        help="A boolean indicating if static diagrams are compiled and exported.",
    )

    # Export the project code to LaTex.
    parser.add_argument(
        "--c2l",
        action="store_true",
        help="A boolean indicating if project code is exported to LaTex.",
    )

    # Export the exporting code, and the project code to LaTex.
    parser.add_argument(
        "--ec2l",
        action="store_true",
        help="A boolean indicating if code that exports code is exported to LaTex.",
    )

    # Load the arguments that are given.
    args = parser.parse_args()
    return args
