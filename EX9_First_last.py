def firstlast(sequence: iter) -> iter:
    return sequence[:1] + sequence[-1:]

def even_odd_sums(sequence: iter) -> list:
    return [sum(sequence[::2]), sum(sequence[1::2])]

def plus_minus(sequence: iter) -> int:
    return sequence[0] + sum(sequence[1::2]) - sum(sequence[2::2])

def myzip(*iterables: iter) -> list[tuple]:
    zipped = []
    length = len(iterables[0]) # 假设所有可迭代对象的长度都相同

    for i in range(length):
        tuple_element = tuple(it[i] for it in iterables)
        zipped.append(tuple_element)

    return zipped


if __name__ == '__main__':
    print(firstlast('abcd'))
    print(firstlast([1, 2, 3, 4]))
    print(firstlast((1, 2, 3, 4)))
    print(firstlast(['a', 'b', 'c', 'd']))
    print(firstlast(('a', 'b', 'c', 'd')))

    print(even_odd_sums([10, 20, 30, 40, 50, 60]))
    print(even_odd_sums((10, 20, 30, 40, 50, 60)))

    print(plus_minus([10, 20, 30, 40, 50, 60]))
    print(plus_minus((10, 20, 30, 40, 50, 60)))

    print(myzip([10, 20,30], 'abc'))