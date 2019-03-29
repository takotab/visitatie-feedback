import os

import pandas as pd
import dominate
from dominate import tags as dt

from .result_figure import make_result_figure
from .utils import make_filename


def make_htmlfile(praktijk: str, visitatie_uitslag: dict = None, unit_test=False):

    filename = make_filename(
        "Feedback visitatie " + praktijk + " 2018",
        folder="result_pdfs",
        unit_test=unit_test,
        file_type=".html",
    )
    doc = dominate.document(title=filename)
    logo = "data_real/result_pdfs/Logo-rug-netwerk_v2.jpg"
    assert os.path.isfile(logo)
    with doc:
        with dt.div(style="width:800px; margin:0 auto;"):
            dt.h1("Feedback Visitatie 2018 - " + praktijk, align="center")
            dt.h4("25 Maart 2019", align="center")
            dt.img(width=600, src=strip_sep(logo), id="header")
            dt.br()
            dt.br()
            dt.div("Beste Rug-netwerker,")
            dt.br()
            dt.div(
                "De visitatieronde is afgerond en de resultaten zijn verwerkt. Hartelijk dank voor het meedoen. "
                + "Het geeft ons inzicht wat er gebeurt in de praktijken en willen dit met jullie delen. Je krijgt feedback op praktijkniveau en je eigen regio."
            )
            dt.br()
            dt.div("Er zijn drie categorieen: Groen, Oranje en Rood.")
            dt.br()
            dt.div(
                "Er zijn duidelijke verschillen tussen praktijken. Daar kunnen logische verklaringen voor zijn. Het kan zijn dat je voor het eerst meedoet of dat er binnen de praktijk andere wisselingen hebben plaats gevonden. Daarom vragen we een reactie als de praktijk in het stoplicht model ROOD scoort."
            )
            dt.br()
            dt.div(
                "Voor de normering wordt gebruik gemaakt van de 6 items. Deze zijn in onderstaande tabel weergegeven."
            )
            dt.br()
            dt.div("beschrijvings_table")
            dt.br()
            dt.div(
                "In de onderstaande tabel zijn de voorwaarde voor de categorieen te vinden. Om een categorie te halen moet aan beide voorwaarden worden voldaan."
            )
            dt.br()
            dt.div("norm_table")
            dt.br()
            dt.div("Uw catagorie is: " + visitatie_uitslag[praktijk]["Catagorie"])
            if visitatie_uitslag[praktijk]["Catagorie"] == "Rood":
                dt.div(
                    "Wij verwachten binnen 2 weken een reactie. Er kunnen verschillende reden zijn waarom dit zo is. Wij zijn hier erg benieuwd naar."
                )
            else:
                dt.br()
                dt.br()

            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.br()
            dt.h2("Resultaten")
            f, df = make_result_figure(praktijk, visitatie_uitslag, unit_test)
            dt.img(src=strip_sep(f))
            dt.div("result_table")

    stoplicht = [
        "2 Dossiers per Therapeut = 100%",
        "Praktijktoets",
        "Dossiertoets",
        "2 meetinstrumenten (incl. begin- en eindmeting)",
        "Gebruik STarTBack",
        "Gebruik GPE ",
    ]
    pd.set_option("display.max_colwidth", -1)
    doc = make_bescrhijving_table(str(doc), stoplicht, "<div>beschrijvings_table</div>")
    doc = make_norm_table(str(doc))
    doc = make_result_table(doc, df)
    with open(filename, "w") as f:
        f.write(str(doc))
    return doc, filename


def replace_keyword(doc: str, keyword: str, item: str):
    return doc.replace(keyword, item)


def _format(x):
    if float(int(x)) == float(x):
        return str(int(x))
    else:
        return "{:.2f}".format(x)


def strip_sep(f: str):
    return f.split(os.sep)[-1]


def make_norm_table(doc):
    return replace_keyword(
        doc,
        "<div>norm_table</div>",
        pd.DataFrame()
        .from_dict(
            {
                "Catagorie": ["Groen", "Oranje", "Rood"],
                "Item 1": ["100%", "100%", "<100%"],
                "Item 2 t/m 6": [
                    "0 of 1 onder de norm",
                    "2 onder de norm",
                    "3 of meer onder de norm",
                ],
            }
        )
        .to_html(float_format=_format),
    )


def make_result_table(doc: str, df: pd.DataFrame):
    return replace_keyword(
        doc, "<div>result_table</div>", df.T.to_html(float_format=_format)
    )


def make_bescrhijving_table(doc: str, stoplicht: list, keyword: str):
    table = (
        pd.DataFrame()
        .from_dict(
            {
                "Item": [str(i) for i in range(1, len(stoplicht) + 1)],
                "Beschrijving (per dossier)": stoplicht,
            }
        )
        .to_html(index=False)
    )
    return replace_keyword(doc, keyword, table)


# def align_td(doc: str):
#     return doc.replace("<td>", "<td align='center'>")

