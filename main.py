import argparse
import os
import logging
import json

import pandas as pd
import pdfkit

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
    go = False
    if os.path.isfile("q_a.csv"):
        os.remove("q_a.csv")
    result_froms = {}
    result = {}
    for i in range(1, 66):
        # print(i)
        a_form = visitatie.get_data(i=i, path=dir)
        if a_form.praktijk_code == 9_999_999:
            continue
        c = visitatie.get_color(a_form)
        print(i, c)
        result[a_form.naam] = c
        result_froms[a_form.naam] = visitatie.get_json_dct(a_form)
    print(len(result), result)
    result_r = {}
    for key, item in result.items():
        _, html_f = visitatie.make_htmlfile(key, result_froms)
        pdfkit.from_file(html_f, html_f.replace(".html", ".pdf"))
        print("made file", key)
        if item in result_r:
            result_r[item].append(key)
        else:
            result_r[item] = [key]
        # if go:  # or key == "Oefentherapie Mensendieck Schagen"
        #     try:
        #         visitatie.send_mail(
        #             **visitatie.make_message(
        #                 key,
        #                 check_email(result_froms[key]["email"]),
        #                 html_f.replace(".html", ".pdf"),
        #             )
        #         )
        #     except:
        #         print("Error in sending email.\nDid not sent email for:", key)
        #         # go = True
    for key in result_r:
        print(f"\n---{key}---\n")
        print("num of praktijken:", len(result_r[key]))
        print(result_r[key])
    print([(len(result_r[key]), key) for key in result_r])
    json.dump(result_froms, open("data_real/results_.json", "w"))
    df = pd.read_json("data_real/results_.json").T
    df.to_csv("results.csv")
    visitatie.all_results(result_froms)
    visitatie.only_regios_results(["nk"])


def check_email(email: str):
    if "/" in email:
        email = email.split("/")[0]
    return email.replace(" ", "")


if __name__ == "__main__":
    main(args.dir)
