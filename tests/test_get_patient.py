import os
import visitatie


def test_get_patient():
    test_f = "visitatie/patient_questions_pytest.txt"
    if os.path.exists(test_f):
        os.remove(test_f)
    visitatie.get_patients.patient_question_file = test_f

    a_form = visitatie.get_data(i=0)
    patient_data = visitatie.get_patient_data(a_form, 0)
    a_form.dct[
        "Therapeutcode van de behandelde therapeut betreffende dit dossier "
    ] = 00
    assert visitatie.get_patient_data(a_form, 0) == patient_data

    patient_data = visitatie.get_patients(a_form)
    assert set(list(patient_data.keys())) == set([0, 1, "last_patient"])
    assert patient_data["last_patient"] == 1

    os.remove(test_f)
