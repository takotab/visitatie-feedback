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
    result["Regio"] = form.regio

    for key, item in form.toetsen.items():
        if key[0] != "_":
            result[key.replace("_", " ")] = item

    return make_all_str(result)


def remove_quotes(*args):
    return [arg.replace('"', "") for arg in args]


def make_all_str(dct: dict, fn: callable = None):
    result = {}
    for key, item in dct.items():
        if fn is not None:
            key, item = fn(key, item)
        result[str(key)] = str(item)
    return result

