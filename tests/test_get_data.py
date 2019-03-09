import visitatie


def test_get_data():
    a_form = visitatie.get_data(i=0)
    assert a_form.naam == "Fysiotherapie Real Madrid"
    assert a_form.bezoekende_therapeut == "Fysiotherapie FC Barcalona"
    
