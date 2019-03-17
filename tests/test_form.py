import visitatie
import pytest


@pytest.mark.raises(exception=FileNotFoundError)
def test_form_find_inschrijving_error():
    f = visitatie.get_data(0)
    f.find_inschrijving_info_code(code=100)


@pytest.mark.raises(exception=FileNotFoundError)
def test_form_aantal_therapeuten_error():
    f = visitatie.get_data(0)
    f.find_aantal_therapeuten(email="abcdefghij@gma1l.c0m")


def test_fix_length():
    str_l = visitatie.form.fix_length(["abc"] * 11)
    assert len(str_l) == 10


def test_not_juiste_bezocht():
    a_form = visitatie.get_data(i=0)
    a_form.check_door_de_juist_bezocht(9623113)
    assert not a_form.door_de_juiste_bezocht


def test_juiste_bezocht_int():
    a_form = visitatie.get_data(i=0)
    a_form.check_door_de_juist_bezocht()
    assert a_form.door_de_juiste_bezocht


def test_get_keys():
    a_form = visitatie.get_data(i=0)
    result = a_form.get_keys(
        [
            "Praktijkcode van de praktijk die bezocht wordt",
            "Therapeutcode bezoekende therapeut?",
        ]
    )
    assert (
        result["Praktijkcode van de praktijk die bezocht wordt"] == a_form.praktijk_code
    )
    assert (
        result["Therapeutcode bezoekende therapeut?"]
        == a_form.bezoekende_therapeut_code
    )
    assert len(result) == 2


@pytest.mark.raises(exception=KeyError)
def test_not_get_keys():
    a_form = visitatie.get_data(i=0)
    result = a_form.get_keys(["ipsus lorum", "Therapeutcode bezoekende therapeut?"])


@pytest.mark.raises(exception=FileNotFoundError)
def test_not_find_plan_b_praktijk():
    a_form = visitatie.get_data(i=0)
    a_form.check_door_de_juist_bezocht(96231131)
    assert not a_form.door_de_juiste_bezocht


def test_empty_keys():
    a_form = visitatie.get_data(i=0)
    all_keys = a_form.get_keys()
    assert all_keys == list(a_form.dct.keys())


# @pytest.mark.raises(exception=KeyError)
def test_99999():
    a_form = visitatie.get_data(i=3)


def test_weird_email():
    a_form = visitatie.get_data(i=4)
