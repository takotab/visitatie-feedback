import os


class Form(object):
    def __init__(self, pd_serie, path):
        self.path = path
        self.dct = dict(pd_serie)
        # TODO get basic info {"naam","naam code","Aantal Therapeuten","bezoekende therapeut code","bezoekende prakijk}
        self.get_basic_info()

    def get_basic_info(self):
        self.praktijk_code = self.dct["Praktijkcode van de praktijk die bezocht wordt"]
        inschrijving_gegevens = self.find_inschrijving_code()
        self.naam = inschrijving_gegevens["naam"]
        self.email = inschrijving_gegevens["email"]
        self.bezoekende_therapeut_code = self.dct["Therapeutcode bezoekende therapeut?"]

    def find_inschrijving_code(self, code=None):
        if code is None:
            code = self.praktijk_code
        with open(os.path.join(self.path, "gegevens.csv")) as f:
            for line in f:
                splited_line = line.replace("\n", "").split(",")
                if len(splited_line) != 10:
                    splited_line[7] = ",".join(splited_line[7:9])
                    splited_line[8:] = splited_line[9:]

                assert len(splited_line) == 10, splited_line
                if splited_line[5] == str(code):
                    return {"naam": splited_line[7], "email": splited_line[9]}
        raise FileNotFoundError(code)
