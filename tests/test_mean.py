import numpy as np

from visitatie.mean import Mean


def test_mean():
    np.random.seed(42)
    lst = [np.random.randint(0, 2) for _ in range(10)]

    mean = Mean()
    for o in lst:
        if len(mean) > 4:
            mean(o)
        else:
            mean.add(o)

    assert mean.mean() == np.mean(lst)
