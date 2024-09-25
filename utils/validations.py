import re


def validate_full_name(full_name: str) -> bool:
    pattern = re.compile('^[A-Za-z][a-z]+(?: [A-Za-z][a-z]+)+$')

    full_name = full_name.strip()
    if re.match(pattern, full_name):
        return True
    else:
        return False


def __erase_whitespace(string: str) -> str:
    while string.__contains__("  "):
        string = string.replace("  ", " ")

    return string.strip()


def string_to_num(string: str) -> int:
    age = 0

    string = __erase_whitespace(string).lower().split(" ")

    if len(string) == 2:
        decimal = {
            "o'n": ten,
            "yigirma": twenty,
            "o'ttiz": thirty,
            "qirq": fourty,
            "ellik": fifty,
            "oltmish": sixty,
            "yetmish": seventy,
            "sakson": eighty,
            "to'qson": ninety,
        }

        age += decimal.get(string[0], lambda: 0)()

        options = {
            "bir": one,
            "ikki": two,
            'uch': three,
            "to'rt": four,
            "besh": five,
            "olti": six,
            "yetti": seven,
            "sakkiz": eight,
            "to'qqiz": nine,
        }

        age += options.get(string[1], lambda: 0)()
        return age

    if len(string) == 1:
        options = {
            "bir": one,
            "ikki": two,
            'uch': three,
            "to'rt": four,
            "besh": five,
            "olti": six,
            "yetti": seven,
            "sakkiz": eight,
            "to'qqiz": nine,
        }

        age += options.get(string[0], lambda: 0)()
        return age

    else:
        return -1


def ten():
    return 10


def twenty():
    return 20


def thirty():
    return 30


def fourty():
    return 40


def fifty():
    return 50


def sixty():
    return 60


def seventy():
    return 70


def eighty():
    return 80


def ninety():
    return 90


def one():
    return 1


def two():
    return 2


def three():
    return 3


def four():
    return 4


def five():
    return 5


def six():
    return 6


def seven():
    return 7


def eight():
    return 8


def nine():
    return 9
