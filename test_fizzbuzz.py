import fizzbuzz as fb
import pytest


def test_dict_load():
    # test that a duplicate entry in the dictionary will give result from the last entry
    testdict = {"3": "teststr1", "5": "teststr1", "5": "teststr2"}
    assert fb.fizzbuzz(15, testdict) == "teststr1teststr2"


def test_no_dictionary():
    # test that trying to open a dictionary that does not exist will give an error
    with pytest.raises(FileNotFoundError):
        with open("invalid_file.json", 'r') as _:
            pass


def test_empty_dictionary():
    # test that giving a dictionary wth no entries will give the same output as input
    out = fb.fizzbuzz(1, {})
    assert out == "1"


@pytest.mark.parametrize(("invaiddict",), [("teststr",), (1,), ({"teststr": "1"},), ({"1": 1},)])
def test_invalid_dictionary_param(invaiddict):
    # test that giving an invalid format of dictionary or non dictionary replacement will raise custom error
    with pytest.raises(fb.InvalidDictionaryError):
        fb.dictionary_checker(invaiddict)


def test_invert_dictionary():
    # test that giving a replacement for multiples of zero will return an error
    with pytest.raises(ZeroDivisionError):
        fb.fizzbuzz(1, {"0": "teststr"})


def test_line_returned_from_fizzbuzz_function():
    # test that fizzbuzz gives out a correct string for a given dictionary
    testdict = {"1": "test1", "2": "test2", "3": "test3", "6": "test6"}
    line = fb.fizzbuzz(6, testdict)
    assert(isinstance(line, str))
    assert(line == "test1test2test3test6")


def test_line_order():
    # test that the order of entries into the dictionary change the order fo the output line
    testdict = {"1": "test1", "2": "test2", "6": "test6", "3": "test3"}
    line = fb.fizzbuzz(6, testdict)
    assert(isinstance(line, str))
    assert(line == "test1test2test6test3")


def test_str_sys_argv():
    # test error returned when giving a str for an input
    with pytest.raises(TypeError):
        fb.main("testsrt")