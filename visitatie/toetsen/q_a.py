import os
import json

filename = "q_a.csv"


def add_single_qa(question: str, answer: float, basetoets: str = None, file=None):
    """This will save all answers on the different questions"""
    if file is None:
        file = filename
    init(file)
    if type(answer) is not str:
        answer = "%.3f" % answer
    with open(file, "a") as f:
        f.write(",".join([handle_q(question), answer, basetoets]) + "\n")


def init(file):
    if not os.path.isfile(file):
        with open(file, "w") as f:
            f.write("question,answer,basetoets\n")


def handle_q(q: str):
    return (
        q[:100]
        .replace(",", "-")
        .replace("é", "e")
        .replace("/", "")
        .replace("\t", "")
        .replace("ï", "i")
        # .replace("")
        .replace("ë", "e")
    )
