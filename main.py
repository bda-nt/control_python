import string
import re


if __name__ == '__main__':
    file = open('inputData/file.input', 'r', encoding='UTF-8')
    dictionary = {}
    for line in file:
        sep_array = string.punctuation + '\n' + ' '
        regex_pattern = '|'.join(map(re.escape, sep_array))
        words = re.split(regex_pattern, line)

        for word in words:
            if len(word) == 0:
                continue

            word = word.lower()
            if word in dictionary.keys():
                dictionary[word] += 1
                continue

            dictionary[word] = 1

    print(dictionary)
