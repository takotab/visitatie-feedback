def make_addition(i: int):
    if i > 11:
        raise FileExistsError(f"Only 12 patients now attemting to acces patient 13")
    return "." + str(i) if i > 0 else ""


def remove_additions(dct: list, i: int) -> dict:
    if i == 0:
        return dct
    result = {}
    for key, item in dct.items():
        result[key.replace("." + str(i), "")] = item
    return result

