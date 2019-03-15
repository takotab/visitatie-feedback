import os
import pytest

import visitatie


def test_get_patient():
    test_f = "visitatie/patient_questions.txt"
    if os.path.exists(test_f):
        os.remove(test_f)

    a_form = visitatie.get_data(i=0)
    patient_data = visitatie.get_patient_data(a_form, 0)
    a_form.dct[
        "Therapeutcode van de behandelde therapeut betreffende dit dossier "
    ] = 00
    assert visitatie.get_patient_data(a_form, 0) == patient_data

    patient_data = visitatie.get_data_from_all_patients(a_form)
    assert set(list(patient_data.keys())) == set([0, 1, "last_patient"])
    assert patient_data["last_patient"] == 1

    os.remove(test_f)


def test_get_patient_2():
    test_f = "visitatie/patient_questions.txt"
    if os.path.exists(test_f):
        os.remove(test_f)

    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    assert a_form.patients["last_patient"] == 3


@pytest.mark.raises(exception=KeyError)
def test_get_patient_error():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    visitatie.get_patient_data(a_form, 3)


@pytest.mark.raises(exception=FileExistsError)
def test_get_patient_3_error():
    a_form = visitatie.get_data(i=2)
    _ = visitatie.get_data_from_all_patients(a_form)
