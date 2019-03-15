from visitatie.toetsen.meetinstrumenten_utils import _meetinstrumenten
from visitatie.form import Form

meetinstrumenten_q = {
    "STarT Back": ["STarT Back Screening Tool", "STarT Back Screening Tool_end"],
    "GPE": ["GPE1", "GPE2"],
}


def get_startback_gpe(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _meetinstrumenten(form.patients[i], i, meetinstrumenten_q)
    result = get_patient_stats(result)
    return result


norms = {"num_start_end": 2, "num_meetinstrumenten_used": 2}


def get_patient_stats(result: dict):
    norm_met = 0
    for _, patient in result.items():
        # meetinstrument_norm_met = 0
        for key, norm in norms.items():
            if patient[key] >= norm:
                norm_met += 1

    result["num_norm_met"] = int(norm_met > 1)
    return result
