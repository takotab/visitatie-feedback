import os
import visitatie

from tests.assets import RESULT_DICT


def test_result_table():
    praktijk = "Tako"

    result_dct = visitatie.make_result(praktijk, RESULT_DICT, unit_test=True)
    assert list(result_dct.keys()) == ["All", "Regio Champions League", "Tako"]
    assert result_dct["Regio Champions League"]["GPE"] == (1 / 3)
    assert result_dct["Regio Champions League"]["Dossier per Therapeut"] == (4 / 3)

    praktijk = "Real Madrid"

    result_dct = visitatie.make_result(praktijk, unit_test=True)
    assert list(result_dct.keys()) == ["All", "Regio Champions League", "Real Madrid"]
    assert result_dct["Regio Champions League"]["GPE"] == (1 / 3)
    assert result_dct["Regio Champions League"]["Dossier per Therapeut"] == (4 / 3)

    os.remove("data_fake/results_mean_Champions League.json")
    os.remove("data_fake/results_mean_All.json")


def test_make_result_figure():
    praktijk = "Real Madrid"
    f = visitatie.make_result_figure(praktijk, RESULT_DICT, unit_test=True)
    assert os.path.isfile(f)
