from src.module.functions import yield_random_identifier

def test_yield_random_identifier():
    real = len(yield_random_identifier())
    expect = 10

    assert real == expect