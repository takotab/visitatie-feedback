import os

import pandas as pd
import dominate
from dominate import tags as dt


def make_htmlfile(praktijk: str, visitatie_uitslag: dict = None, unit_test=False):
    filename = "Feedback visitatie " + praktijk + " 2018"
    doc = dominate.document(title=filename)
    with doc:
        with dt.div(style="width:800px; margin:0 auto;"):
            assert os.path.isfile("Logo-rug-netwerk_v2.jpg")
            dt.h1("Feedback Visitatie 2018 - " + praktijk, align="center")
            dt.h4("25 Maart 2019", align="center")
            dt.img(width=600, src="Logo-rug-netwerk_v2.jpg", id="header")
            dt.br()
            dt.br()
            dt.div("Beste Rug-netwerker,")
            dt.br()  # "    ", width="100%", height="10px"
            dt.div(
                "Allereerst willen wij u bedanken voor het deelnemen aan de visitatieronde afgelopen zomer. Voor een grotegroep was dit de eerste keer dat zij hieraan mee hebben gedaan. Daarnaast zijn er praktijken met meerervaring, zij deden voor de derde of zelfs een vierde keer mee. Het is daarom logisch dat er verschillen zijnontstaan. "
            )
            dt.br()
            dt.div(
                "In de onderstaande gegevens is te zien waar uw praktijkcode staat ten opzichten van het gemiddelde.Er staat tevens waar wij als netwerk naar toe willen: de norm (Groen).Dit is verwerkt in een stoplichtmodel."
            )
            dt.br()
            dt.div(
                "Er zijn drie categorieen: Groen, Oranje en Rood.Voor de normering wordt gebruik gemaakt van de 6 items weergeven in de onderstaande tabel."
            )
            dt.br()
            dt.div("beschrijvings_table")
            dt.br()
            dt.div(
                "In de onderstaande tabel zijn de voorwaarde voor de categorieen te vinden. Om een categorie te behalen moet beide aan voorwaarde worden voldaan."
            )
            dt.div("norm_table")
            dt.br()
            dt.div("Uw catagorie is: " + visitatie_uitslag[praktijk]["Catagorie"])
            if visitatie_uitslag[praktijk]["Catagorie"] == "Rood":
                dt.div(
                    "Wij verwachten binnen 2 weken een reactie. Er kunnen verschillende reden zijn waarom dit zo is. Wij zijn hier erg benieuwd naar."
                )
            dt.h2("Resultaten")
            dt.img(
                src=visitatie.make_result_figure(praktijk, visitatie_uitslag, unit_test)
            )
            dt.dive("result_table")
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

    with open(filename + ".html", "w") as f:
        f.write(str(doc))
    return doc, filename + ".html"


def replace_keyword(doc: str, keyword: str, item: str):
    return doc.replace(keyword, item)


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
