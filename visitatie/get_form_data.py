import pandas as pd
import os

from visitatie.form import Form

path = "data_real"


def get_data(i=0, path="data_fake"):
    f = os.path.join(path, "visitatie_form.csv")
    # f = checkfile(f)
    df = pd.read_csv(f)
    return Form(df.iloc[i, :], path)


# def checkfile(f: str):
#     adjusted = False
#     with open(f, "r") as f:
#         for line in f:
#             new_patients = []
#             patients = line.split("Wilt u nog een patiënt invoeren?,")
#             for patient in patients:
#                 patient_qs = []
#                 for q in patient.split(","):
#                     if q not in patient_qs:
#                         patient_qs.append(q)
#                     else:
#                         new_q = q + "_end"
#                         patient_qs.append(new_q)
#                         adjusted = True
#                 new_patients.append(",".join(patient_qs))
#             new_line = "Wilt u nog een patiënt invoeren?,".join(new_patients)
#             if not adjusted:
#                 return f

#             assert len(new_line.split(",")) == len(line.split(","))
#             print(new_line)
