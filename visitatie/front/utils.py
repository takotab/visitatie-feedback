import os
import pandas as pd
import matplotlib.pyplot as plt


def plt_df(df: pd.DataFrame, filename=None, mycolors=None):
    if mycolors is None:
        mycolors = [
            "tab:pink",
            "tab:blue",
            "tab:brown",
            "tab:purple",
            "tab:orange",
            "tab:red",
            "tab:gray",
            "tab:olive",
            "tab:cyan",
        ]
        mycolors = mycolors[: df.shape[0] - 1] + ["tab:green"]
    assert mycolors[-1] == "tab:green"
    df.T.plot(kind="bar", color=mycolors)
    plt.plot([0, 6], [100, 100], "k-", lw=2)
    plt.ylabel("% of norm")
    plt.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    if filename:
        plt.tight_layout()
        plt.savefig(filename)
    plt.close()


def visitatie_uitslag_filename(unit_test: bool):
    return make_filename(unit_test=unit_test)


def regio_filename(regio: str, unit_test: bool):
    return make_filename("mean", regio, unit_test=unit_test)


def make_filename(*args: [str], folder="", unit_test: bool, file_type=".json"):
    folder_dct = {0: "data_real", 1: "data_fake"}
    args = [arg.replace("/", "").replace('"', "") for arg in args]
    f = folder_dct[int(unit_test)]
    if folder is not "":
        f += "/" + folder
    if not os.path.isdir(f):
        os.mkdir(f)
    return f + "/results_" + "_".join(args) + file_type

