import os
import pytest
import visitatie


def test_get_data():
    a_form = visitatie.get_data(i=0)
    assert a_form.naam == "Fysiotherapie Real Madrid"
    assert a_form.bezoekende_therapeut == "Fysiotherapie FC Barcalona"
    assert a_form.aantal_therapeuten == 2
    assert a_form.door_de_juiste_bezocht


def test_checkfile():
    f = os.path.join("data_fake", "visitatie_form.csv")
    f_new = visitatie.get_form_data.checkfile(f, debug=True)
    check_in_file(f_new)
    f_new2 = visitatie.get_form_data.checkfile(f_new, debug=True)
    assert f_new == f_new2


def test_checkfile_not_debug():
    f = os.path.join("data_fake", "visitatie_form.csv")
    f_new = visitatie.get_form_data.checkfile(f)
    check_in_file(f_new)


def check_in_file(f: str):
    _check_in_file(
        f,
        should_be_s=[
            "STarT Back Screening Tool,",
            "PSK 1,PSK 1_end",
            "PSK 2,PSK 2_end",
            "PSK 3,PSK 3_end,",
            "VAS-P gem,VAS-P gem_end,",
            "NRS,NRS_end,",
        ],
        should_not_be_s=[
            "STarT Back Screening Tool ,",
            "PSK 1,PSK 1,",
            "PSK 2,PSK 2,",
            "PSK 3,PSK 3,",
            "NRS,NRS,",
        ],
    )


def _check_in_file(f: str, should_be_s: [str], should_not_be_s: [str]):
    with open(f, "r") as f:
        for line in f:
            for should_be in should_be_s:
                assert should_be in line
            for should_not_be in should_not_be_s:
                assert should_not_be not in line
            return


@pytest.mark.raises(exception=FileNotFoundError)
def test_file_not_found():
    for i in range(20):
        visitatie.get_data(i)
