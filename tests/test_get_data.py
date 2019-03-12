import pytest
import visitatie


def test_get_data():
    a_form = visitatie.get_data(i=0)
    assert a_form.naam == "Fysiotherapie Real Madrid"
    assert a_form.bezoekende_therapeut == "Fysiotherapie FC Barcalona"
    assert a_form.aantal_therapeuten == 2
    assert a_form.door_de_juiste_bezocht

