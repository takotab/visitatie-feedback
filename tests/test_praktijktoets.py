import visitatie


def test_praktijk_toets():
    a_form = visitatie.get_data(i=0)
    dct = visitatie.praktijk_toets(a_form)
    assert dct["Praktijktoets"] == 0.8
    a_form = visitatie.get_data(i=0)
    dct_t = visitatie.praktijk_toets(a_form, niet_van_toepassing=True)
    assert dct["Praktijktoets"] is not dct_t["Praktijktoets"]

