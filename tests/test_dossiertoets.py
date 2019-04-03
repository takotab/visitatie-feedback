import visitatie


def test_dossier_toets():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _dossiertoets = visitatie.toetsen._dossier_toets(a_form.patients[0], 0)
    assert _dossiertoets["Dossiertoets"] == 0.3333333333333333


def test_dossier_toets_niet_toepassing():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _dossiertoets = visitatie.toetsen._dossier_toets(
        a_form.patients[0], 0, niet_van_toepassing=True
    )
    assert _dossiertoets["Dossiertoets"] == 0.2727272727272727


def test_get_dossiertoets():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _dossiertoets = visitatie.toetsen.get_dossier_toets(a_form)
    assert _dossiertoets["Dossiertoets"] == 0.41666666666666663


def test_get_dossiertoets_2():
    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    _dossiertoets = visitatie.toetsen.get_dossier_toets(a_form)
    assert _dossiertoets["Dossiertoets"] == 0.375
    assert len(_dossiertoets["_dossiertoets"]) == 4

