def pig_latin():
    word = input("Please enter a word: ")
    temp = ''
    if not word[-1].isalpha():
        temp = word[-1]
        word = word[:-1]

    if word[0].lower() in 'aeiou':
        word += 'way'
    else:
        if word[0].isupper():
            word = word[0].lower() + word[1].upper() + word[2:]
        word = word[1:] + word[0] + 'ay'

    if temp:
        print(f"{word}{temp}")
    else:
        print(word)

def pig_latin_new():
    word = input("Please enter a word: ")
    letters = set(word)
    cnt = 0
    for letter in letters:
        if letter in 'aeiou':
            cnt += 1
            if cnt >= 2:
                word += 'way'
                break
    if cnt < 2:
        word = word[1:] + word[0] + 'ay'
    print(word)

if __name__ == '__main__':
    pig_latin_new()