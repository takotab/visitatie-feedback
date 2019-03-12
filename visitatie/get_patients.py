from visitatie.form import Form

PATIENTS_Q = None


def get_patients(form: Form):
    last = False
    i = 0
    while not last:
        last = get_patient_data(form, i, is_last=True)
        i += 1

    return form.patients


def get_patient_data(form: Form, i: int = 0, is_last: bool = False):
    if i in form.patients and not is_last:
        return form.patients[i]

    patient_questions = get_patient_questions(PATIENTS_Q, form)
    check_is_last(form, i)

    form.patients[i] = form.get_keys(
        [key + make_addition(i) for key in patient_questions]
    )
    _is_last = check_this_is_last(form, i)

    if is_last:
        return _is_last
    return form.patients[i]


def get_patient_questions(patient_questions: list, form: Form):
    if patient_questions is None:
        all_keys_w_one = [key for key in form.get_keys() if ".1" in key[-2:]]
        PATIENTS_Q = [key[:-2] for key in all_keys_w_one]
        return PATIENTS_Q
    else:
        return PATIENTS_Q


def check_is_last(form: Form, i: int):

    if form.patients["last_patient"] != "Unknown":
        if i > form.patients["last_patient"]:
            raise KeyError(
                f"{form.naam} only has {form.patients['last_patient']} patients"
            )


def check_this_is_last(form: Form, i: int):
    if form.patients[i]["Wilt u nog een patiënt invoeren?" + make_addition(i)] == "Nee":
        form.patients["last_patient"] = i
        return True
    return False


def make_addition(i: int):
    return "." + str(i) if i > 0 else ""
