import pandas as pd
import os

from visitatie.form import Form

path = "data_real"


def get_data(i=0, real=False, path="data_fake"):
    if real:
        path = "data_real"

    df = pd.read_csv(os.path.join(path, "visitatie_form.csv"))
    return Form(df.iloc[i, :], path)
