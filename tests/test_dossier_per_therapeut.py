import visitatie
import pytest


def test_dossiers_per_therapeut():
    a_form = visitatie.get_data(i=0)
    visitatie.get_data_from_all_patients(a_form)
    dossier_per_therapeut = a_form._check_num_patients()
    assert dossier_per_therapeut == 0.5


@pytest.mark.raises(exception=NotImplementedError)
def test_not__check_num_patients():
    a_form = visitatie.get_data(i=0)
    a_form._check_num_patients()

