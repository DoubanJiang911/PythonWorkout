def strsort(a_string):
    return ''.join(sorted(a_string))

def word_sort(some_string: str):
    words = some_string.split()
    output = []
    for word in words:
        output.append(strsort(word))
    return ','.join(output)

if __name__ == '__main__':
    print(word_sort("Tom Dick Harry,"))