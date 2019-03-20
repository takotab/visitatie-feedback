import os
import pytest

import visitatie

toets_params = [(0, 2), (1, 4), (4, 6)]


@pytest.mark.parametrize("i,expected", toets_params)
def test_get_patient(i, expected):
    test_f = "visitatie/patient_questions.txt"
    if os.path.exists(test_f):
        os.remove(test_f)

    a_form = visitatie.get_data(i=i)
    patient_data = visitatie.get_patient_data(a_form, 0)
    a_form.dct[
        "Therapeutcode van de behandelde therapeut betreffende dit dossier "
    ] = 00
    assert visitatie.get_patient_data(a_form, 0) == patient_data

    visitatie.get_data_from_all_patients(a_form)
    patient_data = a_form.patients
    assert "last_patient" in list(patient_data.keys())
    assert patient_data["last_patient"] == expected

    os.remove(test_f)


def test_get_patient_2():
    test_f = "visitatie/patient_questions.txt"
    if os.path.exists(test_f):
        os.remove(test_f)

    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    assert a_form.patients["last_patient"] == 4


@pytest.mark.raises(exception=KeyError)
def test_get_patient_error():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    visitatie.get_patient_data(a_form, 3)


@pytest.mark.raises(exception=FileExistsError)
def test_get_patient_3_error():
    a_form = visitatie.get_data(i=2)
    _ = visitatie.get_data_from_all_patients(a_form)
