import os
import pytest
import pdfkit

import visitatie
from tests.test_result_table import RESULT_DICT


toets_params = ["Tako", "Fysiotherapiepraktijk Willemsstad"]


@pytest.mark.parametrize("parktijk", toets_params)
def test_make_html(parktijk):
    filename = "test_pdf.pdf"
    doc, html_f = visitatie.make_htmlfile(parktijk, RESULT_DICT, unit_test=True)
    assert type(str(doc)) == str
    assert os.path.isfile(html_f)
    os.remove(filename)
    pdfkit.from_file(html_f, filename)
    assert os.path.isfile(filename)

    print("done")

