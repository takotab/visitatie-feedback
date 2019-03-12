import visitatie


def test_get_patient():
    a_form = visitatie.get_data(i=0)
    visitatie.get_patients(a_form)
