import os

from visitatie import utils


class Form(object):
    def __init__(self, pd_serie, path):
        self.path = path
        self.dct = dict(pd_serie)
        self.door_de_juiste_bezocht = False
        self.patients = {"last_patient": "Unknown"}
        self.toetsen = {}
        self.get_basic_info()

    def get_basic_info(self):
        self.praktijk_code = self.dct["Praktijkcode van de praktijk die bezocht wordt"]
        inschrijving_gegevens = self.find_inschrijving_info_code()
        self.naam = inschrijving_gegevens["naam"]
        self.email = inschrijving_gegevens["email"]
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
        splited_line = utils.v_find(os.path.join(self.path, "gegevens.csv"), code, 5)
        return {
            "naam": splited_line[7],
            "email": splited_line[9],
            "planned_b_praktijk": splited_line[6],
        }

    def find_aantal_therapeuten(self, email: str = None):
        if email is None:
            email = self.email

        return int(
            utils.v_find(
                os.path.join(self.path, "inschrijven_visitatie_2018.csv"), email, 1, 3
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
            result[key] = self.dct[key]
        return result

    def _check_num_patients(self):
        if self.patients["last_patient"] == "Unknown":
            raise NotImplementedError()

        self.toetsen["dossier_per_therapeut"] = (
            self.patients["last_patient"] / self.aantal_therapeuten
        )
        return self.toetsen["dossier_per_therapeut"]

    def add_toets(self, toets_results):
        self.toetsen.update(toets_results)


def therapeut_2_praktijk_code(code):
    code = str(code)
    if len(code) > 7:
        code = code[:7]
    return code


def fix_length(str_lst: [str]):
    if len(str_lst) != 10:
        str_lst[7] = ",".join(str_lst[7:9])
        str_lst[8:] = str_lst[9:]
    assert len(str_lst) == 10
    return str_lst


def find_plan_b_praktijk(praktijk_code, path):
    return utils.v_find(os.path.join(path, "gegevens.csv"), str(praktijk_code), 6, 5)

