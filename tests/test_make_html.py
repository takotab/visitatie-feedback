import os
import pdfkit
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


def test_make_html():
    filename = "test_pdf.pdf"
    doc, html_f = visitatie.make_htmlfile({"naam": "Tako"})
    assert type(str(doc)) == str
    assert os.path.isfile(html_f)
    os.remove(filename)
    pdfkit.from_file(html_f, filename)
    assert os.path.isfile(filename)

    print("done")

