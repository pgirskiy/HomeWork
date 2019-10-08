import re


def letters_only(a: str) -> str:
    '''
    :param a: string
    :return: filtered str
    Using regular expressions, this function filter all characters except Latin
    '''
    let = re.sub(r"[^a-zA-Z]", "", a)
    assert let.isalpha()
    return let

