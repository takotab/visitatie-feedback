import visitatie


def test_dossier_toets():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _dossiertoets = visitatie._dossier_toets(a_form.patients[0])
    assert _dossiertoets == {"Dossiertoets": 0.25}

