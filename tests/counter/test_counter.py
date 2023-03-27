from src.pre_built.counter import count_ocurrences


def test_counter():
    path = 'data/jobs.csv'
    word = 'a'

    counter = count_ocurrences(path, word)
    assert counter == 705686
