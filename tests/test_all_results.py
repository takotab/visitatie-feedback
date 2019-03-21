import os
import visitatie



def test_all_results():
    f = visitatie.all_results(unit_test=True)
    assert os.path.isfile(f)

