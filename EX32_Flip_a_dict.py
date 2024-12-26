import os
import glob

def flipped_dict(a_dict):
    return {value: key
            for key, value in a_dict.items()}

def vowel_count(word):
    total = 0
    for one_letter in word.lower():
        if one_letter in 'aeiou':
            total += 1
    return total

def dict_of_vowels(input_str: str) -> dict:
    return {word: vowel_count(word)
            for word in input_str.split()}

def file_info(dirname):
    return {one_filename[2:]: os.stat(one_filename).st_size
            for one_filename in glob.glob(f'{dirname}/*')
            if os.path.isfile(one_filename)}


print(flipped_dict({'a':1, 'b':2, 'c':3}))

print(dict_of_vowels("this is an easy test."))

print(file_info('.'))