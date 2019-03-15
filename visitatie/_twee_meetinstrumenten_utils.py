import numpy as np

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


def _twee_meetinstrumenten(antworden: dict):
    result = {}
    for instrument, instrument_qs in meetinstrumenten_q.items():
        instrument_a = {key: antworden[key] for key in instrument_qs}
        instrument, instrument_a = modify_anders(instrument, instrument_a)
        result[instrument] = _instrument(instrument_a)
    result = get_stats(result)
    return result


def _instrument(antworden: dict):
    result = {"start_end": True, "used": False}
    for _, item in antworden.items():
        if np.isnan(item):
            result["start_end"] = False
        else:
            result["used"] = True
    return result


def modify_anders(instrument, instrument_a):
    if instrument == "Anders":
        instrument = instrument_a["Welk ander meetinstrument gebruikt u?"]
        del instrument_a["Welk ander meetinstrument gebruikt u?"]
    return instrument, instrument_a


def get_stats(result: dict):
    num_used, num_start_end = 0, 0
    used_meet_instrumenten = []
    for instrument in result:
        if result[instrument]["used"]:
            num_used += 1
            if result[instrument]["start_end"]:
                num_start_end += 1
                used_meet_instrumenten.append(instrument)
    result["num_meetinstrumenten_used"] = num_used
    result["num_start_end"] = num_start_end
    result["used_meet_instrumenten"] = used_meet_instrumenten
    return result
