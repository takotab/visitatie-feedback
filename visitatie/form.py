import os
import json
import pandas as pd
from visitatie import utils

inschrijven_visitatie_csv = "inschrijven_visitatie.csv"
gegevens_csv = lambda path: os.path.join(path, "gegevens.csv")


class Form(object):
    def __init__(self, pd_serie, path):
        self.path = path
        self.dct = dict(pd_serie)
        self.door_de_juiste_bezocht = False
        self.patients = {"last_patient": "Unknown"}
        self.toetsen = {}
        self.q_answers = {}
        self.get_basic_info(path)

    def get_basic_info(self, path: str):
        self.praktijk_code = self.dct["Praktijkcode van de praktijk die bezocht wordt"]
        if self.praktijk_code == int(9_999_999):
            return self
        print("self.praktijk_code:", self.praktijk_code)
        inschrijving_gegevens = self.find_inschrijving_info_code()
        for key, item in inschrijving_gegevens.items():
            setattr(self, key, item)
        self.naam = inschrijving_gegevens["naam"]
        self.email = inschrijving_gegevens["email"]
        check_if_all_have_been(path, self.email)
        self.aantal_therapeuten = self.find_aantal_therapeuten()
        self.bezoekende_therapeut_code = self.dct["Therapeutcode bezoekende therapeut?"]
        self.bezoekende_praktijk = therapeut_2_praktijk_code(
            self.bezoekende_therapeut_code
        )
        self.check_door_de_juist_bezocht()
        self.bezoekende_therapeut = self.find_inschrijving_info_code(
            code=self.bezoekende_praktijk
        )["naam"]

    def find_inschrijving_info_code(self, code=None):
        if code is None:
            code = self.praktijk_code
        code = therapeut_2_praktijk_code(code)
        df = pd.read_csv(gegevens_csv(self.path))
        df = df[df["naam code"] == int(code)]
        assert df.shape[0] == 1, code
        dct = dict(df.iloc[0, :])
        assert "@" in str(dct["email"]), str(dct["email"])
        return {
            "naam": dct["praktijknaam"],
            "email": dct["email"],
            "planned_b_praktijk": dct["bezoekende prakijk"],
            "regio": dct["regio"],
        }

    def find_aantal_therapeuten(self, email: str = None):
        if email is None:
            email = self.email
        df = pd.read_csv(os.path.join(self.path, inschrijven_visitatie_csv))
        df = df[df["E-mailadres"] == self.email]
        assert df.shape[0] == 1, f"{df.shape}, {self.email}"
        return int(df["Aantal Rug-Netwerk therapeuten in de praktijk"].values)
        try:
            return int(
                utils.v_find(
                    os.path.join(self.path, inschrijven_visitatie_csv),
                    email,
                    1,
                    3,
                )
            )
        except:
            print(email)
            return int(
                utils.v_find(
                    os.path.join(self.path, inschrijven_visitatie_csv),
                    email.split("@")[-1].split(".")[0],
                    1,
                    3,
                    _in=True,
                )
            )

    def check_door_de_juist_bezocht(self, praktijk_code=None):
        if praktijk_code is None:
            praktijk_code = self.praktijk_code
        planned_b_praktijk = find_plan_b_praktijk(praktijk_code, self.path)

        self.door_de_juiste_bezocht = self.bezoekende_praktijk == planned_b_praktijk
        if not self.door_de_juiste_bezocht:
            print(
                f"WARNING:{self.naam} is niet door de juiste bezocht./n{self.bezoekende_therapeut_code} is not {planned_b_praktijk}"
            )
            # pdb.set_trace()
        self.toetsen["door_de_juiste_bezocht"] = self.door_de_juiste_bezocht

    def get_keys(self, keys: list = None):
        if keys is None:
            return list(self.dct.keys())
        result = {}
        for key in keys:
            if key in self.dct:
                result[key] = self.dct[key]
            else:
                print(self.dct.keys())
                raise KeyError(key)
        return result

    def _check_num_patients(self):
        if self.patients["last_patient"] == "Unknown":
            raise NotImplementedError()

        self.toetsen["dossier_per_therapeut"] = (
            self.patients["last_patient"] / self.aantal_therapeuten
        )
        self.toetsen["_dossier_per_therapeut"] = {
            "aantal_theraputen": self.aantal_therapeuten,
            "Aantal dossiers": self.patients["last_patient"],
        }
        return self.toetsen["dossier_per_therapeut"]

    def add_toets(self, toets_results: dict):
        self.toetsen.update(toets_results)


def therapeut_2_praktijk_code(code):
    code = str(code)
    if len(code) > 7:
        code = code[:7]
    return code


from typing import List


def fix_length(str_lst: List[str]):
    if len(str_lst) != 10:
        str_lst[7] = ",".join(str_lst[7:9])
        str_lst[8:] = str_lst[9:]
    assert len(str_lst) == 10
    return str_lst


def find_plan_b_praktijk(praktijk_code, path):
    df = pd.read_csv(gegevens_csv(path))
    df = df[df["naam code"] == praktijk_code]
    return df["bezoekende prakijk"].values
    # return utils.v_find(, str(praktijk_code), 6, 5)


def check_if_all_have_been(path: str, email: str):
    f = os.path.join(path, "email_not_yet_done.json")
    if not os.path.exists(f):
        make_not_yet(f, path)
    not_yet = json.load(open(f, "r"))
    if email in not_yet["not_yet"]:
        not_yet["not_yet"].remove(email)
    not_yet["done"].append(email)
    json.dump(not_yet, open(f, "w"))


def make_not_yet(f_not_yet: str, path: str):
    emails = list(pd.read_csv(gegevens_csv(path))["email"])
    result = {"not_yet": emails}
    result["done"] = []
    json.dump(result, open(f_not_yet, "w"))
