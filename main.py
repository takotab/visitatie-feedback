import argparse
import os
import logging

import visitatie

parser = argparse.ArgumentParser(description="Handeling the results of the visitatie.")

parser.add_argument(
    "--dir",
    default="data_real",
    type=str,
    help="Select the map to be used for making the results.",
)
args = parser.parse_args()


def main(dir):
    for i in range(4, 10):
        a_form = visitatie.get_data(i=i, path=dir)
        if a_form.bezoekende_therapeut_code == 999999901:
            break
        print(i, visitatie.get_color(a_form))

    # TODO Save praktijk_dict as json
    # TODO make pdf rapport
    pass


if __name__ == "__main__":
    main(args.dir)
