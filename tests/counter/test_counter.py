from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    
    assert count_ocurrences(path, "Python") == 1639, "A contagem para 'Python' está incorreta."
    assert count_ocurrences(path, "JavaScript") == 122, "A contagem para 'JavaScript' está incorreta."
