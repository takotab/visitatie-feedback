import pandas as pd
import os

from visitatie.form import Form

path = "data_real"


def get_data(i=0, path="data_fake"):
    f = os.path.join(path, "visitatie_form.csv")
    # f = checkfile(f)
    df = pd.read_csv(f)
    return Form(df.iloc[i, :], path)


def checkfile(f_path: str):
    adjusted = False
    new_file = ""
    with open(f_path, "r") as f:
        first_line = True
        for line in f:
            if first_line:
                new_patients = []
                patients = line.split("Wilt u nog een patiënt invoeren?,")
                for patient in patients:
                    patient_qs = []
                    for q in patient.split(","):
                        if "STarT Back Screening Tool " in q:
                            q = q.replace(
                                "STarT Back Screening Tool ",
                                "STarT Back Screening Tool",
                            )
                            adjusted = True
                        if q not in patient_qs:
                            patient_qs.append(q)
                        else:
                            new_q = q + "_end"
                            patient_qs.append(new_q)
                            adjusted = True
                    new_patients.append(",".join(patient_qs))

                new_line = "Wilt u nog een patiënt invoeren?,".join(new_patients)

                if not adjusted:
                    return f_path
                assert len(new_line.split(",")) == len(line.split(","))
                new_file += new_line + os.linesep
                first_line = False
            else:
                new_file += line + os.linesep

    with open(new_file_name(f_path), "w") as f_new:
        f_new.write(new_file)
    return new_file_name(f_path)


def new_file_name(f: str):
    return f.replace(".csv", "_adjusted.csv")

