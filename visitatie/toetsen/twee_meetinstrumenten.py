from visitatie.form import Form


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _twee_meetinstrumenten(form.patients[i])
    return result


meetinstrumenten_q = {
    "VAS": [
        "VAS-P gem",
        "VAS-P gem_end",
        "VAS-P min",
        "VAS-P min_end",
        "VAS-P max",
        "VAS-P max_end",
    ],
    "PSK": ["PSK 1", "PSK 1_end", "PSK 2", "PSK 2_end", "PSK 3", "PSK 3_end"],
    "NRS": ["NRS", "NRS_end"],
    "QBPDS": ["QBPDS", "QBPDS_end"],
    "Anders": ["Welk ander meetinstrument gebruikt u?", "Anders", "Anders_end"],
}
# STarT Back Screening Tool,STarT Back Screening Tool_end,GPE1,GPE2


def _twee_meetinstrumenten(antworden: dict, negatief="niet aanwezig"):
    return {"twee_meetinstrumenten": 0.25}

