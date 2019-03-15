import visitatie


def test_twee_meetinstrumenten():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    _twee_meetinstrumenten = visitatie.toetsen._twee_meetinstrumenten(
        a_form.patients[0]
    )
    assert _twee_meetinstrumenten == {"twee_meetinstrumenten": 0.25}

