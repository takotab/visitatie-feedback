import numpy as np
import pandas as pd
import yaml
import argparse
import os

parser = argparse.ArgumentParser(description="Handeling the results of the visitatie.")

parser.add_argument(
    "--dir",
    default="data_real",
    type=str,
    help="Select the map to be used for making the results.",
)
args = parser.parse_args()


def ifna(row: pd.Series):
    if pd.isnull(row["praktijknaam"]):
        return row["Wat is de naam van de praktijk?"]
    return row["praktijknaam"]


def main(path):
    df = pd.read_csv(os.path.join(path, "Indeling 2020 - View.csv"))
    df = df.dropna(subset=["naam code"])
    df["naam code"] = df["naam code"].astype(int)
    df["regio"] = df["naam code"].apply(lambda x: int(str(x)[0]))
    df["praktijknaam"] = df.apply(ifna, 1)
    df["bezoekende prakijk"] = df["2020 bezoekende praktijk"]
    df = df[df["Doet mee 2020 (dt)"] != "0"]
    df["email"] = df["E-mailadres"]
    df = df[["regio", "naam code", "praktijknaam", "bezoekende prakijk", "email"]]
    df.to_csv(os.path.join(path, "gegevens.csv"), index=False)


if __name__ == "__main__":
    main(args.dir)