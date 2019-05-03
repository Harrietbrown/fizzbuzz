import fizzbuzz
import pytest


def test_dict_load():
    replacements = {"3": "fizz", "5": "buzz", "5": "fizz"}
    assert replacements == {"3": "fizz", "5": "fizz"}


def test_no_dictionary():
    with pytest.raises(FileNotFoundError):
        with open("invalid_file.json", 'r') as dictionary:

def test_

