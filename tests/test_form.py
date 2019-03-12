import visitatie
import pytest


# def test_form_find_inschrijving():
#     f = visitatie.get_data(0)
#     with pytest.raises(FileExistsError):
#         f.find_inschrijving_info_code(code=100)


def test_fix_length():
    str_l = visitatie.form.fix_length(["abc"] * 11)
    assert len(str_l) == 10


def test_not_juiste_bezocht():
    a_form = visitatie.get_data(i=0)
    a_form.check_door_de_juist_bezocht("08" + str(a_form.bezoekende_therapeut_code))
    assert not a_form.door_de_juiste_bezocht


def test_juiste_bezocht_int():
    a_form = visitatie.get_data(i=0)
    a_form.check_door_de_juist_bezocht(a_form.bezoekende_praktijk)
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


def test_not_get_keys():
    a_form = visitatie.get_data(i=0)
    try:
        result = a_form.get_keys(["ipsus lorum", "Therapeutcode bezoekende therapeut?"])
        assert False
    except KeyError as e:
        assert True
