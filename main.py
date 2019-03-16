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
    result = {}
    for i in range(4, 100):
        a_form = visitatie.get_data(i=i, path=dir)
        if a_form.praktijk_code == 9999999:
            continue
        c = visitatie.get_color(a_form)
        print(i, c)
        result[a_form.naam] = c
    # TODO Save praktijk_dict as json
    # TODO make pdf rapport
    print(len(result), result)


if __name__ == "__main__":
    main(args.dir)
