from visitatie.form import Form
from visitatie.mean import Mean


def get_dossier_toets(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _dossier_toets(form.patients[i])
    return result


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


def _dossier_toets(antworden: dict, negatief="niet aanwezig", niet_van_toepassing=True):

    mean = Mean()
    for item in [antworden[q] for q in dossier_toets_q]:
        if "niet van toepassing" not in item and niet_van_toepassing:
            mean(negatief not in item)
    return {"Dossiertoets": mean.mean()}