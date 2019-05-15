import json
import pandas as pd

from .utils import plt_df, make_filename, visitatie_uitslag_filename
from .result_overview import find_mean_regio
from .result_figure import cols


def all_results(visitatie_uitslag: dict = None, unit_test=False):

    return only_regios_results(visitatie_uitslag=visitatie_uitslag, unit_test=unit_test)


def only_regios_results(
    regios: list = ["all"], visitatie_uitslag: dict = None, unit_test=False
):
    if visitatie_uitslag is None:
        visitatie_uitslag = json.load(open(visitatie_uitslag_filename(unit_test)))

    f = make_filename(
        "_".join(regios) + "results", unit_test=unit_test, file_type=".png"
    )
    if regios == ["all"]:
        regios = find_regios(visitatie_uitslag)

    df_ = make_plotdf_regios(visitatie_uitslag, regios, unit_test)
    plt_df(df_, filename=f)
    return f


def make_plotdf_regios(
    visitatie_uitslag, regios, unit_test, incl_norm=True, incl_all=True
):
    if incl_all:
        regios.append("All")
    overiew_dct = {}
    for regio in regios:
        overiew_dct[regio] = find_mean_regio(regio, visitatie_uitslag, unit_test)

    df = pd.DataFrame().from_dict(overiew_dct).T
    if incl_norm:
        df_ = df.loc[:, cols]
        df_.loc["Norm", cols] = [2, 0.7, 1, 0.7, 1, 1]
        df_ = df_ / df_.loc["Norm", :] * 100

    return df_


def find_regios(visitatie_uitslag: dict):
    regios = []
    for key in visitatie_uitslag:
        if visitatie_uitslag[key]["Regio"] not in regios:
            regios.append(visitatie_uitslag[key]["Regio"])
    return regios
