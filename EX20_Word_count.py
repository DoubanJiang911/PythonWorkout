import os
from collections import Counter

def wordcount(filename: str) -> None:
    counts = {'characters': 0, 'words': 0, 'lines': 0}
    unique_words = set()
    for one_line in open(filename, encoding='utf-8'):
        counts['lines'] += 1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())
        unique_words.update(one_line.split())

    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')

def count_word_frequencies() -> dict:
    file_path = input("Enter the name of a text file: ")
    words = input("Enter words separated by spaces: ").split()

    word_count = dict.fromkeys(words, 0)
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for word in words:
                word_count[word] += line.lower().count(word.lower())
    return word_count


def file_sizes() -> dict:
    directory = input("Enter the directory path: ")
    size_dict = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            size_dict[filename] = os.stat(file_path).st_size
    return size_dict

def letter_frequencies():
    directory = input("Enter the directory path: ")
    letter_count = Counter()
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                contents = file.read().lower()
                letter_count.update(char for char in contents if char.isalpha())
    return letter_count.most_common(5)

if __name__ == '__main__':
    wordcount('test_file.txt')

    print("==========Beyond the exercise1==========")
    frequencies  = count_word_frequencies()
    for output_word, count in frequencies.items():
        print(f"{output_word}: {count}")

    # print("==========Beyond the exercise2==========")
    # # Example usage:
    # file_sizes_dict = file_sizes()
    # for file, size in file_sizes_dict.items():
    #     print(f"{file}: {size} bytes")

    # print("==========Beyond the exercise3==========")
    # # Example usage:
    # most_common_letters = letter_frequencies()
    # for letter, frequency in most_common_letters:
    #     print(f"{letter}: {frequency}")