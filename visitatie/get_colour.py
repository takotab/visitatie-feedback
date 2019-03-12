from visitatie.form import Form
from visitatie.praktijktoets import praktijk_toets
from visitatie import get_data_from_all_patients
from visitatie.dossier_toets import get_dossier_toets


def get_colour(form: Form):
    form.praktijktoets = praktijk_toets(form)
    _ = get_data_from_all_patients(form)
    _ = get_dossier_toets(form)
    return "green"

