def ubbi_dubbi(word: str) -> str:
    output = []

    if word[0].isupper() and word[0] in 'AEIOU':
        output.append(f'Ub{word[0].lower()}')
    elif word[0].islower() and word[0] in 'aeiou':
        output.append(f'ub{word[0]}')
    else:
        output.append(word[0])

    for letter in word[1:]:
        if letter in 'aeiou':
            output.append('ub')
        output.append(letter)

    return ''.join(output)

def remove_author_names(article: str, authors_names: list[str]) -> str:
    """
    # another solution
    words = article.split()
    output = []
    for word in words:
        if word in authors_names:
            output.append('_' * len(word))
        else:
            output.append(word)
    return ' '.join(output)
    """

    for name in authors_names:
        article = article.replace(name, '_'*len(name))
    return article

def url_encode(s):
    # Initialize an empty list to store the encoded characters
    encoded_chars = []

    # Iterate over each character in the string
    for char in s:
        # Check if the character is a letter or a number
        if char.isalnum():
            # If it is, append the character as is
            encoded_chars.append(char)
        else:
            # If it's not, replace it with % followed by the hex representation of the character
            encoded_chars.append('%' + hex(ord(char))[2:].upper())

    # Join all the encoded characters into a single string
    return ''.join(encoded_chars)


if __name__ == '__main__':
    print(ubbi_dubbi('ecvp'))

    article_text = "This paper discusses the work of Alice and Bob on the new algorithm. Alice and Charlie have previously worked on similar projects."
    authors_list = ["Alice", "Bob", "Charlie"]
    print(remove_author_names(article_text , authors_list))

    # Example usage:
    original_string = "This is a test string with special characters: !@#$%^&*()"
    encoded_string = url_encode(original_string)
    print(encoded_string)