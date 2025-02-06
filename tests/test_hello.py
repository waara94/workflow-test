from src.app.hello import gen_set


def test_gen_set():
    assert gen_set() == {1, 2, 3}


def test_hello():
    assert True
