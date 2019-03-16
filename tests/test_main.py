import pytest

import visitatie


def test_main():
    a_form = visitatie.get_data(i=0)
    colour = visitatie.get_color(a_form)
    assert type(colour) == str


toets_params = [
    (
        {
            "dossier_per_therapeut": 0.5,
            "praktijktoets": 0.8571428571428571,
            "Dossiertoets": 0.25,
            "twee_meetinstrumenten": 1,
            "startback_gpe": 0,
        },
        "Rood",
    ),
    (
        {
            "dossier_per_therapeut": 1,
            "praktijktoets": 0.9928571428571,
            "Dossiertoets": 0.25,
            "twee_meetinstrumenten": 1,
            "startback_gpe": 1,
        },
        "Oranje",
    ),
    (
        {
            "dossier_per_therapeut": 1,
            "praktijktoets": 0.9928571428571,
            "Dossiertoets": 1,
            "twee_meetinstrumenten": 1,
            "startback_gpe": 1,
        },
        "Groen",
    ),
]


@pytest.mark.parametrize("test_input,expected", toets_params)
def test_get_colour(test_input, expected):
    color = visitatie.calc_color(test_input)
    assert color["color"] == expected
