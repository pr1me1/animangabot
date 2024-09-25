from constants.constants import UZ, RU, EN
from constants.languages import TRANSLATIONS


def translate(attribute: str, language: str) -> str:
    if not language:
        language = EN

    return TRANSLATIONS.get(attribute).get(language)
