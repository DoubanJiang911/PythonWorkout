from collections import Counter

def most_repeating_word(sequence) -> str:
    dict_list = []
    for index, word in enumerate(sequence):
        cnt = Counter(word).most_common(1)[0][1]
        temp_dict = {'index': index, 'cnt': cnt}
        dict_list.append(temp_dict)
    max_dict = max(dict_list, key=lambda x: x['cnt'])
    max_index = max_dict['index']
    return sequence[max_index]

def most_repeating_vowels_count(word):
    vowels = 'aeiou'
    vowel_counts = Counter(letter for letter in word if letter in vowels)
    if vowel_counts:
        return vowel_counts.most_common(1)[0][1]
    else:
        return 0

def most_repeated_vowels(sequence) -> str:
    return max(sequence, key = most_repeating_vowels_count)



if __name__ == '__main__':
    words = ['this', 'is', 'an', 'elementary', 'test', 'abracadabra', 'bbbbbbbbbb', 'example']
    print(most_repeating_word(words))

    print(most_repeated_vowels(words))
