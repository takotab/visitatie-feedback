from visitatie.toetsen.meetinstrumenten_utils import (
    _meetinstrumenten,
    get_patient_stats,
)
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


norms = {
    "num_start_end": 2,
    #  "num_meetinstrumenten_used": 2,
}


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _meetinstrumenten(form.patients[i], i, meetinstrumenten_q)

    return {
        "twee_meetinstrumenten": get_patient_stats(result, norms),
        "_twee_meetinstrumenten": result,
    }

