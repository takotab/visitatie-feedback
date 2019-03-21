import pandas as pd
import matplotlib.pyplot as plt


def plt_df(df: pd.DataFrame, filename=None):
    df.T.plot(kind="bar", color=["tab:blue", "tab:orange", "tab:green"])
    plt.plot([0, 6], [100, 100], "k-", lw=2)
    plt.ylabel("% of norm")
    if filename:
        plt.tight_layout()
        plt.savefig(filename)


def visitatie_uitslag_filename(unit_test: bool):
    return make_filename(unit_test=unit_test)


def regio_filename(regio: str, unit_test: bool):
    return make_filename("mean", regio, unit_test=unit_test)


def make_filename(*args: [str], unit_test: bool, file_type=".json"):
    folder = {0: "data_real", 1: "data_fake"}
    return folder[int(unit_test)] + "/results_" + "_".join(args) + file_type

