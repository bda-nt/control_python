import string
import re

filename = 'inputData/file.input'
mode = 'r'
encoding = 'UTF-8'


def read_file() -> string:
    """
    Считывает файл и возвращает строки лениво
    :return: Строка файла
    :rtype: str
    """
    with open(filename, 'r', encoding='UTF-8') as file:
        for line in file:
            yield line.rstrip()


def make_dictionary(text: list) -> dict:
    """
    Создает словарь из массива переданного в метод
    :param text: Массив строк считаных с файла
    :return: Словарь { "value": str => "value_count": int }
    :rtype: dict
    """
    dictionary = {}

    for line in text:
        sep_array = string.punctuation + '\n' + ' '
        # regex pattern !|"|\#|\$|%|\&|'|\(|\)|\*|\+|,|\-|\.|/|:|;|<|=|>|\?|@|\[|\\|\]|\^|_|`|\{|\||\}|\~|\n|\W
        regex_pattern = '|'.join(map(re.escape, sep_array))
        # чистка от спец символов, через regex иначе длинный набор инструкций через str.split()
        words = re.split(regex_pattern, line)

        # Запись слов в словарь
        for word in words:
            # игнорирование пустых строк
            if len(word) == 0:
                continue

            # перевод в нижний регистр
            word = word.lower()
            if word in dictionary.keys():
                dictionary[word] += 1
                continue

            dictionary[word] = 1

    return dictionary


if __name__ == '__main__':
    data_from_file = [line for line in read_file()]

    print(make_dictionary(data_from_file))
