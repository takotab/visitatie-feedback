from visitatie.form import Form
from visitatie.toetsen import (
    praktijk_toets,
    get_dossier_toets,
    get_meetinstrumenten,
    get_startback_gpe,
)
from visitatie.get_patients import get_data_from_all_patients


def get_colour(form: Form):
    form.praktijktoets = praktijk_toets(form)
    _ = get_data_from_all_patients(form)
    _ = get_dossier_toets(form)
    _ = get_meetinstrumenten(form)
    _ = get_startback_gpe(form)
    return "green"


def excecute_tasks(form: Form, tasks: list):
    for task in tasks:
        form.add_toets(task(form))
