from visitatie.toetsen._twee_meetinstrumenten_utils import _twee_meetinstrumenten
from visitatie.form import Form


def get_meetinstrumenten(form: Form):
    result = {}
    for i in range(form.patients["last_patient"]):
        result[i] = _twee_meetinstrumenten(form.patients[i], i)
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

