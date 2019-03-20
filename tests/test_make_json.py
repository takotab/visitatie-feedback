import visitatie

example_keys = [
    "naam",
    "email",
    "Praktijkcode",
    "Aantal Dossiers",
    "Aantal Therapeuten",
    "Bezoekende Praktijkcode",
    "Door de juiste bezocht",
    "Dossier per Therapeut",
    "door de juiste bezocht",
    "dossier per therapeut",
    "Praktijktoets",
    "Dossiertoets",
    "twee meetinstrumenten",
    "STarTBack",
    "GPE",
    "Catagorie",
    "Score",
]


def test_make_json_dct():
    a_form = visitatie.get_data(0)
    _ = visitatie.get_color(a_form)
    json_dct = visitatie.get_json_dct(a_form)

    for key in example_keys:
        assert key in json_dct
