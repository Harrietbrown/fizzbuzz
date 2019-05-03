import fizzbuzz
import pytest


def test_dict_load():
    replacements = {"3": "fizz", "5": "buzz", "5": "fizz"}
    assert replacements == {"3": "fizz", "5": "fizz"}


def test_no_dictionary():
    with pytest.raises(FileNotFoundError):
        with open("invalid_file.json", 'r') as dictionary:
            pass


def test_empty_dictionary():
    out = fizzbuzz.fizzbuzz(1, {})
    assert out == "1"


def test_str_dictionary():
    with pytest.raises(fizzbuzz.InvalidDictionaryError):
        fizzbuzz.dictionary_checker("teststr")


def test_int_dictionary():
    with pytest.raises(fizzbuzz.InvalidDictionaryError):
        fizzbuzz.dictionary_checker(1)


def test_invert_dictionary():
    with pytest.raises(fizzbuzz.InvalidDictionaryError):
        fizzbuzz.dictionary_checker({"teststr": "1"})


def test_invert_dictionary():
    with pytest.raises(ZeroDivisionError):
        fizzbuzz.fizzbuzz(1, {"0": "test_str"})


