import pymorphy3
from fuzzywuzzy import fuzz


def check_word_func(list_word: list, word: str) -> str:
    morph = pymorphy3.MorphAnalyzer()
    num_percent = 0
    for el in list_word:
        if fuzz.partial_ratio(word, morph.normal_forms(el)) > num_percent:
            num_percent = fuzz.partial_ratio(word, morph.normal_forms(el))

    return num_percent


def func_del_morthy(list_word: list) -> str:
    morth = pymorphy3.MorphAnalyzer()
    text = list()
    for el in list_word:
        varib = morth.normal_forms(el)[0]
        if 'NOUN' in morth.parse(varib)[0].tag:
            text.append(el)

    return ' '.join(text)


# morth = pymorphy3.MorphAnalyzer(lang='ru')
# print('NOUN' in morth.parse('сочи')[0].tag)
