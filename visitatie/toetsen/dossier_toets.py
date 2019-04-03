from visitatie.form import Form
from visitatie.mean import Mean
from visitatie.utils import remove_additions


def get_dossier_toets(form: Form):
    results = {}
    for i in range(form.patients["last_patient"]):
        results[i] = _dossier_toets(form.patients[i], i)
    return {"_dossiertoets": results, "Dossiertoets": get_stats(results)}


def get_stats(results: dict):
    q_mean = Mean("Dossiertoets")
    dossiertoets_mean = Mean()
    for _, patient_results in results.items():
        for question, item in patient_results.items():
            if question == "Dossiertoets":
                dossiertoets_mean.add(item)
            else:
                q_mean.add(item, question)
    q_mean.mean()
    return dossiertoets_mean.mean()


dossier_toets_q = [
    "Zijn de verwijsgegevens aanwezig in het dossier?",
    "Is de conclusie van de screening aanwezig?",
    "Is de hulpvraag van de patiënt vastgelegd?",
    "Zijn alle domeinen van de ICF beoordeeld binnen het diagnostisch proces?",
    "Is de oefen/ fysiotherapeutische diagnose aanwezig?",
    "Is er een behandeldoel vastgelegd? (concreet, meetbaar, eventueel SMART)",
    "Is het behandelplan opgesteld?    ",
    "Is er in het behandelplan rekening gehouden met de uitslag van de STarT Back Screening Tool? ",
    "Voldoet het dossier aan de minimale-klinimetrie eisen van 2 volledig ingevulde meetinstrumenten naast de STarT Back ?",
    "Wordt er op systematische wijze gebruik gemaakt van klinimetrie?",
    "Wordt er geëvalueerd op de gestelde behandeldoelen en indien nodig bijgesteld?",
    "Is er, kijkend naar de dagjournaals, een systematiek in het therapeutisch handelen terug te vinden?( Hier wordt bedoeld op de relatie met het behandeldoel en het behandelplan)",
]


def _dossier_toets(
    antworden: dict, i: int, negatief="niet aanwezig", niet_van_toepassing=False
):
    antworden = remove_additions(antworden, i)
    mean = Mean()
    result = {}
    for q, item in {q: antworden[q] for q in dossier_toets_q}.items():
        if "niet van toepassing" in str(item).lower() and niet_van_toepassing:
            result[q] = None
            continue
        mean(negatief not in item)
        result[q] = int(negatief not in item)
    result["Dossiertoets"] = mean.mean()
    return result
