import visitatie


def test_praktijk_toets():
    a_form = visitatie.get_data(i=0)
    dct = visitatie.praktijk_toets(a_form)
    assert dct["praktijktoets"] == 0.8571428571428571
    a_form = visitatie.get_data(i=0)
    dct_t = visitatie.praktijk_toets(a_form, niet_van_toepassing=False)
    assert dct["praktijktoets"] is not dct_t["praktijktoets"]
