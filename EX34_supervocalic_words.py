def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return {word.strip()
            for line in open(filename)
            for word in line.split()
            if vowels < set(word.lower())}

print(get_sv('test.txt'))