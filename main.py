import argparse
import os
import logging

import visitatie

parser = argparse.ArgumentParser(description="Handeling the results of the visitatie.")

parser.add_argument(
    "--map",
    default="data_fake",
    type=str,
    help="Select the map to be used for making the results.",
)
args = parser.parse_args()


def main(map):
    a_form = visitatie.get_data(i=0)
    visitatie.get_colour(a_form)

    # TODO STartBack/GPE
    # TODO Save praktijk_dict as json
    # TODO make pdf rapport
    pass


if __name__ == "__main__":
    main(args.map)
