from visitatie.toetsen.meetinstrumenten_utils import (
    _meetinstrumenten,
    get_patient_stats,
)
from visitatie.form import Form

meetinstrumenten_q = {
    "STarTBack": ["STarT Back Screening Tool", "STarT Back Screening Tool_end"],
    "GPE": ["GPE1", "GPE2"],
}


norms = {
    "num_start_end": 2,
    # "num_meetinstrumenten_used": 2
}


def get_startback_gpe(form: Form):
    result = {}
    keys = ["STarTBack", "GPE"]
    for key in keys:
        result.update(_start_gpe(form, key))
    return result


def _start_gpe(form: Form, key: str):

    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _meetinstrumenten(
            form.patients[i], i, {key: meetinstrumenten_q[key]}
        )
    return {"_" + key: result, key: get_patient_stats(result, norms)}

