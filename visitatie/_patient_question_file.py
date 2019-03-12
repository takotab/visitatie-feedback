import os

from visitatie.form import Form

patient_question_file = "visitatie/patient_questions.txt"


def get_patient_questions(form: Form):
    if not os.path.exists(patient_question_file):
        return make_patient_question_file(form)
    else:
        patient_questions = getattr(form, "patient_questions", None)
        if patient_questions is None:
            patient_questions = read_patient_question_file()
        return patient_questions


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
