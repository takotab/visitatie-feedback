from visitatie.form import Form
from visitatie.mean import Mean

praktijk_toets_vragen = [
    "Heeft de praktijk een zodanige behandel/ oefenruimte dat de ADL activiteiten tillen/ dragen,duwen/ trekken, (gaan)zitten/ (gaan)staan, (trap)lopen en springen kunnen worden geoefend?",
    "Heeft de praktijk een zodanig geoutilleerde behandel/ oefenruimte dat uithoudingsvermogen en kracht kan worden getest en getraind?",
    "Wordt er bij afwezigheid van een netwerktherapeut waargenomen door een andere netwerktherapeut binnen zo nodig buiten de praktijk waardoor de continuïteit van de behandeling en neventaken volgens het protocol zijn gewaarborgd?",
    "Vindt er registratie plaats hoeveel geïncludeerde lage rugklachten patiënten behandeld worden?",
    "Is tenminste één netwerktherapeut per praktijk aanwezig geweest bij de verplichte bijeenkomsten/ scholingsdagen?",
    "Heeft de praktijk een verbeterplan opgesteld naar aanleiding van de laatste visitatie?",
    "Kan de praktijk aantoonbaar maken dat het verbeterplan is toegepast?",
]


def praktijk_toets(form: Form, niet_van_toepassing=True, **kwargs):
    antworden = form.get_keys(praktijk_toets_vragen)
    return _praktijk_toets(antworden, niet_van_toepassing=True, **kwargs)


def _praktijk_toets(
    antworden: dict, negatief="niet aanwezig", niet_van_toepassing=False
):
    mean = Mean("Praktijktoets")
    for q, item in antworden.items():
        if "niet van toepassing" in str(item).lower() and niet_van_toepassing:
            continue
        mean(negatief not in item, q)
    return {"Praktijktoets": mean.mean()}
