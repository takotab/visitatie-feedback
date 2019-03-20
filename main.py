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
    result_froms = {}
    result = {}
    for i in range(4, 66):
        a_form = visitatie.get_data(i=i, path=dir)
        if a_form.praktijk_code == 9_999_999:
            continue
        c = visitatie.get_color(a_form)
        print(i, c)
        result[a_form.naam] = c
        result_froms[a_form.praktijk_code] = a_form
    # TODO Save praktijk_dict as json
    # TODO make pdf rapport
    print(len(result), result)
    result_r = {}
    for key, item in result.items():
        if item in result_r:
            result_r[item].append(key)
        else:
            result_r[item] = [key]
    for key in result_r:
        print(f"\n---{key}---\n")
        print("num of praktijken:", len(result_r[key]))
        print(result_r[key])
    print([(len(result_r[key]), key) for key in result_r])


if __name__ == "__main__":
    main(args.dir)
