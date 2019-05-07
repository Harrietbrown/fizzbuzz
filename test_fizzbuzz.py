import fizzbuzz as fb
import pytest


def test_dict_load():
    replacements = {"3": "fizz", "5": "buzz", "5": "fizz"}
    assert replacements == {"3": "fizz", "5": "fizz"}


def test_no_dictionary():
    with pytest.raises(FileNotFoundError):
        with open("invalid_file.json", 'r') as dictionary:
            pass


def test_empty_dictionary():
    out = fb.fizzbuzz(1, {})
    assert out == "1"


@pytest.mark.parametrize(("invaiddict",), [("teststr",), (1,), ({"teststr": "1"},), ({"1": 1},)])
def test_str_dictionary_param(invaiddict):
    with pytest.raises(fb.InvalidDictionaryError):
        fb.dictionary_checker(invaiddict)


def test_invert_dictionary():
    with pytest.raises(ZeroDivisionError):
        fb.fizzbuzz(1, {"0": "teststr"})


def test_line_returned_from_fizzbuzz_function():
    testdict = {"1": "test1", "2": "test2", "3": "test3", "6": "test6"}
    line = fb.fizzbuzz(6, testdict)
    assert(isinstance(line, str))
    assert(line == "test1test2test3test6")


def test_line_order():
    testdict = {"1": "test1", "2": "test2", "6": "test6", "3": "test3"}
    line = fb.fizzbuzz(6, testdict)
    assert(isinstance(line, str))
    assert(line == "test1test2test6test3")




