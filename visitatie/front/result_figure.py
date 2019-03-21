import pandas as pd
from .utils import plt_df, make_filename
from .result_overview import make_result

cols = [
    "Dossier per Therapeut",
    "Dossiertoets",
    "GPE",
    "Praktijktoets",
    "STarTBack",
    "dossier per therapeut",
    "twee meetinstrumenten",
]


def make_result_figure(
    praktijk: str, visitatie_uitslag: dict = None, unit_test=False
) -> str:
    overiew_table = make_result(praktijk, visitatie_uitslag, unit_test)
    df = pd.DataFrame().from_dict(overiew_table).T
    df_ = df.loc[:, cols]
    df_.loc["Norm", cols] = [2, 0.7, 1, 0.7, 1, 2, 1]
    df_ = df_ / df_.loc["Norm", :] * 100
    f = make_filename("plot", praktijk, unit_test=unit_test, file_type=".png")
    plt_df(df_.iloc[1:, :], filename=f)
    return f, df
