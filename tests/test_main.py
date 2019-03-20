import pytest

import visitatie


def test_main():
    a_form = visitatie.get_data(i=0)
    colour = visitatie.get_color(a_form)
    assert type(colour) == str


toets_params = [
    (
        {
            "dossier_per_therapeut": 2,
            "Praktijktoets": 0.9,
            "Dossiertoets": 0.25,
            "twee_meetinstrumenten": 1,
            "STarTBack": 0,
            "GPE": 0.8,
        },
        "Rood",
    ),
    (
        {
            "dossier_per_therapeut": 2,
            "Praktijktoets": 0.9,
            "Dossiertoets": 0.9,
            "twee_meetinstrumenten": 2,
            "STarTBack": 0,
            "GPE": 0.8,
        },
        "Oranje",
    ),
    (
        {
            "dossier_per_therapeut": 1,
            "Praktijktoets": 0.9928571428571,
            "Dossiertoets": 0.25,
            "twee_meetinstrumenten": 1,
            "STarTBack": 1,
            "GPE": 1,
        },
        "Rood",
    ),
    (
        {
            "dossier_per_therapeut": 2,
            "Praktijktoets": 0.9928571428571,
            "Dossiertoets": 1,
            "twee_meetinstrumenten": 2,
            "STarTBack": 1,
            "GPE": 1,
        },
        "Groen",
    ),
]


@pytest.mark.parametrize("test_input,expected", toets_params)
def test_get_colour(test_input, expected):
    color = visitatie.calc_color(test_input)
    assert color["Catagorie"] == expected
