import visitatie


def test_get_patient():
    a_form = visitatie.get_data(i=0)
    patients_data = visitatie.get_patients(a_form)
    print(patients_data)
