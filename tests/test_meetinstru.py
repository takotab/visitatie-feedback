import visitatie


def test_twee_meetinstrumenten():
    a_form = visitatie.get_data(i=0)
    _ = visitatie.get_data_from_all_patients(a_form)
    twee_meetinstrumenten = visitatie.get_meetinstrumenten(a_form)

    assert twee_meetinstrumenten["twee_meetinstrumenten"][0]["num_start_end"] == 2
    assert twee_meetinstrumenten["twee_meetinstrumenten"]["num_norm_met"] == 1


def test_twee_meetinstrumenten_patients():
    a_form = visitatie.get_data(i=1)
    _ = visitatie.get_data_from_all_patients(a_form)
    visitatie.get_meetinstrumenten(a_form)

