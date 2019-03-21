import os
import visitatie

RESULT_DICT = {
    "Tako": {
        "naam": "Tako",
        "email": "tako.oefentherapie+tako@gmail.com",
        "Praktijkcode": "1110111",
        "Aantal Dossiers": "4",
        "Aantal Therapeuten": "2",
        "Bezoekende Praktijkcode": "1110112",
        "Door de juiste bezocht": "True",
        "Dossier per Therapeut": "2.0",
        "Regio": "Champions League",
        "door de juiste bezocht": "True",
        "Praktijktoets": "1.0",
        "Dossiertoets": "1.0",
        "twee meetinstrumenten": "1",
        "STarTBack": "1",
        "GPE": "1",
        "Catagorie": "Groen",
        "Score": "3",
    },
    "Real Madrid": {
        "naam": "Real Madrid",
        "email": "tako.oefentherapie+real@gmail.com",
        "Praktijkcode": "1110111",
        "Aantal Dossiers": "4",
        "Aantal Therapeuten": "2",
        "Bezoekende Praktijkcode": "1110112",
        "Door de juiste bezocht": "True",
        "Dossier per Therapeut": "1.0",
        "Regio": "Champions League",
        "door de juiste bezocht": "True",
        "Praktijktoets": "1.0",
        "Dossiertoets": "1.0",
        "twee meetinstrumenten": "1",
        "STarTBack": "1",
        "GPE": "0",
        "Catagorie": "Groen",
        "Score": "3",
    },
}


def test_result_table():
    praktijk = "Tako"

    result_dct = visitatie.make_result(praktijk, RESULT_DICT, unit_test=True)
    assert list(result_dct.keys()) == ["All", "Regio Champions League", "Tako"]
    assert result_dct["Regio Champions League"]["GPE"] == 0.5
    assert result_dct["Regio Champions League"]["Dossier per Therapeut"] == 1.5

    praktijk = "Real Madrid"

    result_dct = visitatie.make_result(praktijk, unit_test=True)
    assert list(result_dct.keys()) == ["All", "Regio Champions League", "Real Madrid"]
    assert result_dct["Regio Champions League"]["GPE"] == 0.5
    assert result_dct["Regio Champions League"]["Dossier per Therapeut"] == 1.5

    os.remove("data_fake/results_mean_Champions League.json")
    os.remove("data_fake/results_mean_All.json")
