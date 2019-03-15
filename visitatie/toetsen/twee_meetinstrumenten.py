from visitatie.toetsen.meetinstrumenten_utils import _meetinstrumenten
from visitatie.form import Form

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


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _meetinstrumenten(form.patients[i], i, meetinstrumenten_q)
    result = get_patient_stats(result)
    return result


norms = {
    "num_start_end": 2,
    #  "num_meetinstrumenten_used": 2,
}


def get_patient_stats(result: dict):
    norm_met = 0
    for _, patient in result.items():
        # meetinstrument_norm_met = 0
        for key, norm in norms.items():
            if patient[key] >= norm:
                norm_met += 1

    result["num_norm_met"] = norm_met
    return result

