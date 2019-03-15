from visitatie.form import Form


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _twee_meetinstrumenten(form.patients[i])
    return result


def _twee_meetinstrumenten(antworden: dict, negatief="niet aanwezig"):
    return {"twee_meetinstrumenten": 0.25}

