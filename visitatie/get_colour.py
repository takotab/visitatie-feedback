from visitatie.form import Form
from visitatie.toetsen import praktijk_toets
from visitatie.toetsen import get_dossier_toets
from visitatie.get_patients import get_data_from_all_patients


def get_colour(form: Form):
    form.praktijktoets = praktijk_toets(form)
    _ = get_data_from_all_patients(form)
    _ = get_dossier_toets(form)
    return "green"

