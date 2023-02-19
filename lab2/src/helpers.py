import re
from typing import List


def calculate_amount_of_sentences(text: str) -> int:
    regex = r'(\.|\?|!)+'
    return len([*re.finditer(regex, text)])


def calculate_amount_of_non_declarative_sentences(text: str) -> int:
    regex = r'\.+'
    return len([*re.finditer(regex, text)])


def mean(list_of_numbers: List[float]) -> float:
    return sum(list_of_numbers) / len(list_of_numbers)


def calculate_length_of_each_word(text: str) -> List[int]:
    regex = f'\w*[a-zA-Z]\w*'
    words = re.findall(regex, text)
    return list(map(lambda word: len(word), words))


def calculate_average_length_of_words(text: str) -> float:
    return mean(calculate_length_of_each_word(text))


def contains_words(text: str) -> bool:
    regex = f'\w*[a-zA-Z]\w*'
    return bool(re.search(regex, text))


def calculate_average_length_of_sentences(text: str) -> float:
    regex = r'(\.|\?|!)+'
    sentences = filter(contains_words, re.split(regex, text))
    return mean(list(map(lambda word: sum(calculate_length_of_each_word(word)), sentences)))
