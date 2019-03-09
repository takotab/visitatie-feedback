import visitatie


def test_get_data():
    a_form = visitatie.get_data(i=0)
    a_form.naam = "Fysiotherapie FC Barcalona"
    assert True
