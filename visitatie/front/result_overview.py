import os
import json

import pandas as pd

from .utils import visitatie_uitslag_filename, regio_filename

cols = [
    "Aantal Therapeuten",
    "Dossier per Therapeut",
    "Dossiertoets",
    "GPE",
    "Praktijktoets",
    "STarTBack",
    "twee meetinstrumenten",
    "Catagorie",
    "Regio",
]

def make_result(praktijk: str, visitatie_uitslag: dict = None, unit_test=False):
    if visitatie_uitslag is None:
        visitatie_uitslag = json.load(open(visitatie_uitslag_filename(unit_test)))
    result = {}
    result["All"] = find_mean_regio(
        regio="All", visitatie_uitslag=visitatie_uitslag, unit_test=unit_test
    )
    regio = visitatie_uitslag[praktijk]["Regio"]
    result["Regio " + regio] = find_mean_regio(
        regio=regio, visitatie_uitslag=visitatie_uitslag, unit_test=unit_test
    )
    result[praktijk] = {}
    for c in cols[:-2]:
        result[praktijk][c] = float(visitatie_uitslag[praktijk][c])
    return result


def find_mean_regio(regio: str, visitatie_uitslag: dict, unit_test=False):

    filename = regio_filename(regio, unit_test)
    if not os.path.isfile(filename):
        return make_find_mean_regio(regio, visitatie_uitslag, filename)
    return json.load(open(filename, "r"))


def make_find_mean_regio(regio: str, visitatie_uitslag: dict, filename: str):
    df_small = pd.DataFrame().from_dict(visitatie_uitslag).T

    mask = [True] * df_small.shape[0]
    if regio != "All":
        mask = df_small["Regio"] == regio
    result = {}
    for c in cols[:-2]:
        result[c] = df_small.loc[mask, c].astype(float).mean(0)

    json.dump(result, open(filename, "w"))
    return result
