import matplotlib.pyplot as plt


def plt_df(df, filename=None):
    df.T.plot(kind="bar")
    plt.plot([0, 6], [100, 100], "k-", lw=2)
    plt.ylabel("% of norm")
    if filename:
        plt.savefig(filename)


def visitatie_uitslag_filename(unit_test: bool):
    folder = {0: "data_real", 1: "data_fake"}
    return folder[int(unit_test)] + "/results.json"


def regio_filename(regio: str, unit_test: bool):
    folder = {0: "data_real", 1: "data_fake"}
    return folder[int(unit_test)] + "/result_mean_" + regio + ".json"
