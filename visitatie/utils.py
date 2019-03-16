import os


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


def v_find(path: str, match: str, match_col: int, return_col: int = None):
    for line in lines_from_csv_file(path):
        if match == str(line.split(",")[match_col]):
            if return_col is None:
                return line.split(",")
            return line.split(",")[return_col]

    raise FileNotFoundError(match)


def lines_from_csv_file(file):
    with open(file) as f:
        for line in f:
            try:
                yield line.replace("\n", "")
            except GeneratorExit:
                pass
