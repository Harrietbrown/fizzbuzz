import json


class InvalidDictionaryError(Exception):
    def __str__(self):
        return "dictionary.json is in an invalid format entries must be in form of \"int\":\"text\""


def fizzbuzz(val, replacements):
    line = ""
    for num in replacements.keys():
        if val % int(num) == 0:
            line += replacements[num]

    if line == "":
        return str(val)
    else:
        return line


def dictionary_checker(replacements):
    try:
        assert isinstance(replacements, dict)
        for key in replacements.keys():
            int(key)
            assert isinstance(replacements[key], str)
    except:
        raise InvalidDictionaryError


def main():
    with open("dictionary.json", 'r') as dictionary:
        replacements = json.load(dictionary)
        dictionary_checker(replacements)
    n = 100
    for i in range(n):
        print(fizzbuzz(i+1, replacements))
    return


if __name__ == "__main__":
    main()


