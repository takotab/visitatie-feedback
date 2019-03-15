import visitatie


def test_twee_meetinstrumenten():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _twee_meetinstrumenten = visitatie.toetsen._twee_meetinstrumenten(
        a_form.patients[0]
    )
    assert _twee_meetinstrumenten["num_meetinstrumenten_used"] == 4
    assert _twee_meetinstrumenten["num_start_end"] == 2


def test_twee_meetinstrumenten_patients():
    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    visitatie.get_meetinstrumenten(a_form)

