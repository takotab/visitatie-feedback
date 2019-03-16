from visitatie.toetsen.meetinstrumenten_utils import (
    _meetinstrumenten,
    get_patient_stats,
)
from visitatie.form import Form

meetinstrumenten_q = {
    "STarT Back": ["STarT Back Screening Tool", "STarT Back Screening Tool_end"],
    "GPE": ["GPE1", "GPE2"],
}


norms = {
    "num_start_end": 2,
    # "num_meetinstrumenten_used": 2
}


def get_startback_gpe(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _meetinstrumenten(form.patients[i], i, meetinstrumenten_q)
    return {"_startback_gpe": result, "startback_gpe": get_patient_stats(result, norms)}

