import os
from visitatie.form import Form
from visitatie._patient_question_file import *


def get_data_from_all_patients(form: Form):
    last = False
    i = 0
    while not last:
        last = get_patient_data(form, i, is_last=True)
        i += 1
    form._check_num_patients()
    return form.patients


def get_patient_data(form: Form, i: int = 0, is_last: bool = False):
    if i in form.patients and not is_last:
        return form.patients[i]

    patient_questions = get_patient_questions(form)
    check_is_last(form, i)

    form.patients[i] = form.get_keys(
        [key + make_addition(i) for key in patient_questions]
    )
    _is_last = check_this_is_last(form, i)

    if is_last:
        return _is_last
    return form.patients[i]


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

