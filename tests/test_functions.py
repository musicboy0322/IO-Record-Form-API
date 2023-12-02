from cmath import exp
from src.module.functions import split_amount_result, split_total_amount, yield_random_identifier, change_to_json
import json

def test_yield_random_identifier():
    real = len(yield_random_identifier())
    expect = 10

    assert real == expect

def test_change_to_json():
    real = change_to_json(((1, '25845638', 20231104, '1816', '固體', '吃飯', 23, 0, 1), (2, '25845638', 20231104, '2016', '液體', '點滴', 40, 0, 2)))
    expect = '[[1, "25845638", 20231104, "1816", "\u56fa\u9ad4", "\u5403\u98ef", 23, 0, 1], [2, "25845638", 20231104, "2016", "\u6db2\u9ad4", "\u9ede\u6ef4", 40, 0, 2]]'
    assert real == expect

    real = change_to_json(((1, '25845638', 20231104, '1816', '固體', '吃飯', 23, 0, 1)))
    expect = '[1, "25845638", 20231104, "1816", "\u56fa\u9ad4", "\u5403\u98ef", 23, 0, 1]'
    assert real == expect

def test_split_amount_result():
    real = split_amount_result('((1,),)')
    expect = 1
    assert real == expect

def test_split_total_amount():
    real = split_total_amount("((Decimal('23'),),)")
    expect = 23
    assert real == expect