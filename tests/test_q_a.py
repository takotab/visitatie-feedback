import os

from visitatie.toetsen.q_a import add_single_qa


def test_add_single_qa():
    file = "q_a_test.csv"
    add_single_qa("Status"*20, "Nominal", "ISS", file=file)
    add_single_qa("Trottle/", 0, "ISS", file=file)
    assert os.path.isfile(file)
    with open(file, "r") as f:
        for line in f:
            splitted = line.split(",")
            assert len(splitted) == 3
            assert len(splitted[0]) < 101

    os.remove(file)
