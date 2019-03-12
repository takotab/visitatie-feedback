import os
from visitatie.form import Form

patient_question_file = "visitatie/patient_questions.txt"


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

    patient_questions = get_patient_questions(form)
    check_is_last(form, i)

    form.patients[i] = form.get_keys(
        [key + make_addition(i) for key in patient_questions]
    )
    _is_last = check_this_is_last(form, i)

    if is_last:
        return _is_last
    return form.patients[i]


def get_patient_questions(form: Form):
    if not os.path.exists(patient_question_file):
        return make_patient_question_file(form)
    else:
        patient_questions = getattr(form, "patient_questions", None)
        if patient_questions is None:
            patient_questions = read_patient_question_file()
        return patient_questions


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


def make_patient_question_file(form: Form):
    all_keys_w_one = [key for key in form.get_keys() if ".1" in key[-2:]]
    patient_questions = [key[:-2] for key in all_keys_w_one]
    with open(patient_question_file, "w") as f:
        for q in patient_questions:
            f.write(q + "\n")
    print(
        f"made new patient question file. Saved at {patient_question_file}.\nWith {len(patient_questions)} questions."
    )
    return patient_questions


def read_patient_question_file():
    result = []
    with open(patient_question_file, "r") as f:
        for line in f:
            result.append(line.replace("\n", ""))
    return result

