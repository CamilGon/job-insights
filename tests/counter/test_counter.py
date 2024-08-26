from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"

    assert count_ocurrences(path, "Python") == 1639
    assert count_ocurrences(path, "JavaScript") == 122
