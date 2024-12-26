from multiprocessing.managers import Value


def mysum(*numbers, output = 0):
    if numbers and hasattr(numbers[0], '__iter__') and not isinstance(numbers[0], str):
        for number in numbers[0]:
            output += number
    else:
        for number in numbers:
            output += number

    return output

def myavg(numbers: list):
    if not numbers:
        return 0
    return mysum(n for n in numbers) / len(numbers)

def word_lengths(words: list[str]) -> tuple[int, int, int]:
    ln = len(words)
    if ln == 0:
        max_length = min_length = avg_length = 0
    elif ln == 1:
        max_length = min_length = avg_length = len(words[0])
    else:
        max_length = min_length = sum_length = len(words[0])
        for i in range(1, ln):
            if max_length < len(words[i]):
                max_length = len(words[i])
            if min_length > len(words[i]):
                min_length = len(words[i])
            sum_length += len(words[i])
        avg_length = sum_length / ln

    return max_length, min_length, avg_length
        
def sum_ints(objects):
    total = 0
    for obj in objects:
        try:
            total += int(obj)
        except (ValueError, TypeError):
            pass
    return total

if __name__ == "__main__":
    print(mysum(1, 2, 3, 4, 5, output=10))
    print(mysum(10, 20, 30, 40))

    print(myavg([10, 20, 30, 40]))

    print(word_lengths(["hello", "world", "python", "programming"]))

    print(sum_ints([1, 2, 'a', '3', 4.5, '5']))