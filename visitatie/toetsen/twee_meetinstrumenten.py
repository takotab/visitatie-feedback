from visitatie._twee_meetinstrumenten_utils import _twee_meetinstrumenten
from visitatie.form import Form


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _twee_meetinstrumenten(form.patients[i])
    result = get_patient_stats(result)
    return result


def get_patient_stats(result: dict):

    return result


