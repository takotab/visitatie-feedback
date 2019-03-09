import os


class Form(object):
    def __init__(self, pd_serie, path):
        self.path = path
        self.dct = dict(pd_serie)
        self.get_basic_info()

    def get_basic_info(self):
        self.praktijk_code = self.dct["Praktijkcode van de praktijk die bezocht wordt"]
        inschrijving_gegevens = self.find_inschrijving_info_code()
        self.naam = inschrijving_gegevens["naam"]
        self.email = inschrijving_gegevens["email"]
        self.aantal_therapeuten = self.find_aantal_therapeuten()
        self.bezoekende_therapeut_code = self.dct["Therapeutcode bezoekende therapeut?"]
        self.bezoekende_therapeut = self.find_inschrijving_info_code(
            code=str(self.bezoekende_therapeut_code)[:-2]
        )["naam"]

    def find_inschrijving_info_code(self, code=None):
        if code is None:
            code = self.praktijk_code

        for line in lines_from_csv_file(os.path.join(self.path, "gegevens.csv")):
            splited_line = fix_length(line.split(","))

            if splited_line[5] == str(code):
                return {"naam": splited_line[7], "email": splited_line[9]}

        raise FileNotFoundError(code)

    def find_aantal_therapeuten(self, email: str = None):
        if email is None:
            email = self.email

        for line in lines_from_csv_file(
            os.path.join(self.path, "inschrijven_visitatie_2018.csv")
        ):
            if email == str(line.split(",")[1]):
                return int(line.split(",")[3])

        raise FileNotFoundError(email)


def lines_from_csv_file(file):
    with open(file) as f:
        for line in f:
            try:
                yield line.replace("\n", "")
            except GeneratorExit:
                pass


def fix_length(str_lst: [str]):
    if len(str_lst) != 10:
        str_lst[7] = ",".join(str_lst[7:9])
        str_lst[8:] = str_lst[9:]
    assert len(str_lst) == 10
    return str_lst
