import os
import visitatie

from tests.test_result_table import RESULT_DICT


def test_all_results():
    f = visitatie.all_results(RESULT_DICT, unit_test=True)
    assert os.path.isfile(f)
    f = visitatie.all_results(unit_test=True)

