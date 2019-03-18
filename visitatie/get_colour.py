from collections import namedtuple
from visitatie.form import Form
from visitatie.toetsen import (
    praktijk_toets,
    get_dossier_toets,
    get_meetinstrumenten,
    get_startback_gpe,
)
from visitatie.get_patients import get_data_from_all_patients


def get_color(form: Form):
    form.praktijktoets = praktijk_toets(form)
    get_data_from_all_patients(form)
    excecute_tasks(
        form,
        [
            praktijk_toets,
            get_dossier_toets,
            get_meetinstrumenten,
            get_startback_gpe,
            get_form_color,
        ],
    )
    return form.toetsen["color"]


def excecute_tasks(form: Form, tasks: list):
    for task in tasks:
        form.add_toets(task(form))


class Color(object):
    def __init__(self, score):
        color = {0: "Rood", 1: "Oranje", 2: "Groen"}
        self.score = score
        self.i = max([0, score])
        self.color = color[self.i]

    def __str__(self):
        return self.color


toets_norms = {
    "dossier_per_therapeut": 1,
    "praktijktoets": 0.88,
    "Dossiertoets": 0.88,
    "twee_meetinstrumenten": 1,
    "startback_gpe": 1,
}


def get_form_color(form: Form):
    return calc_color(form.toetsen)


def calc_color(toetsen: dict):
    score = 2
    for key, toets_norm in toets_norms.items():
        if toetsen[key] < toets_norm:
            score -= 1

    if toetsen["dossier_per_therapeut"] < 1:
        score -= 1
    c = Color(score)
    return {"color": str(c), "_color": c}
