import visitatie


def test_startback_gpe():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    startback_gpe = visitatie.get_startback_gpe(a_form)

    assert startback_gpe["_startback_gpe"][0]["num_start_end"] == 1
    assert startback_gpe["startback_gpe"] == 0


def test_twee_meetinstrumenten_patients():
    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    visitatie.get_meetinstrumenten(a_form)

