def pig_latin(word: str) -> str:
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
        return f"{word}{temp}"
    else:
        return word

def pl_sentence(words: str) -> str:
    output = []
    word_list = words.split()
    for word in word_list:
        output.append(pig_latin(word))
    return ' '.join(output)

def create_nonsensical_sentence(file_path, n):
    with open(file_path, 'r') as file:
        sentences = []
        for i, line in enumerate(file):
            if i >= 10:  # Only consider the first 10 lines
                break
            words = line.split()
            if len(words) >= n:
                sentences.append(words[n - 1])  # n-1 because list indices start at 0
        return ' '.join(sentences)

def transpose_strings(string_list):
    # Split each string into words and store in a list of lists
    word_lists = [s.split() for s in string_list]
    # Use zip with * to transpose the list of lists
    transposed = zip(*word_lists)
    # Join the words in each group back into a string and return the list of strings
    return [' '.join(group) for group in transposed]

def find_404_errors(logfile_path):
    with open(logfile_path, 'r') as logfile:
        for line in logfile:
            if ' 404 ' in line:
                ip_address = line.split()[0]
                print(ip_address)


if __name__ == '__main__':
    print(pl_sentence('this is a test translation'))

    # Example usage:
    # Assuming 'text_file.txt' is your text file and you want the 3rd word from each line
    print(create_nonsensical_sentence('text_file.txt', 3))

    # Example usage:
    print(transpose_strings(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']))

    # Example usage:
    # Assuming 'apache_log.log' is your Apache logfile
    find_404_errors('apache_log.log')