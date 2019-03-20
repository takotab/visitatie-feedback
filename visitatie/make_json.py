from visitatie.form import Form


def get_json_dct(form: Form):
    result = {}
    result["naam"] = form.naam
    result["email"] = form.email
    result["Praktijkcode"] = form.praktijk_code
    result["Aantal Dossiers"] = form.patients["last_patient"]
    result["Aantal Therapeuten"] = form.aantal_therapeuten
    result["Bezoekende Praktijkcode"] = form.bezoekende_praktijk
    result["Door de juiste bezocht"] = form.door_de_juiste_bezocht
    result["Dossier per Therapeut"] = form.toetsen["dossier_per_therapeut"]
    for key, item in form.toetsen.items():
        if key[0] != "_":
            result[key.replace("_", " ")] = item

    return result

