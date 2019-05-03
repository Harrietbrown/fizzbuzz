import json


def fizzbuzz(val, replacements):
    line = ""
    for num in replacements.keys():
        if val % int(num) == 0:
            line += replacements[num]

    if line == "":
        return str(val)
    else:
        return line


def main():
    with open("dictionary.json", 'r') as dictionary:
        replacements = json.load(dictionary)
    n = 15
    for i in range(n):
        print(fizzbuzz(i+1, replacements))
    return


if __name__ == "__main__":
    main()


