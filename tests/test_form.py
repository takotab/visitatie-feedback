import visitatie
import pytest


# def test_form_find_inschrijving():
#     f = visitatie.get_data(0)
#     with pytest.raises(FileExistsError):
#         f.find_inschrijving_info_code(code=100)


def test_fix_length():
    str_l = visitatie.form.fix_length(["abc"] * 11)
    assert len(str_l) == 10
