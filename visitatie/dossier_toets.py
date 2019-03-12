from visitatie.form import Form


def get_dossier_toets(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _dossier_toets(form.patients[i])
    return result


def _dossier_toets(answers: dict, i=0):
    return 1
