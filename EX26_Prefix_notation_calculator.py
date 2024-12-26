import operator

def calc(to_solve):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, first_s, second_s = to_solve.split()
    first = int(first_s)
    second = int(second_s)
    return operations[op](first, second)

def calc_expand(to_solve: str):
    operations = {'+': operator.add,
                  '-': operator.sub,
                  '*': operator.mul,
                  '/': operator.truediv,
                  '**': operator.pow,
                  '%': operator.mod}
    op, nums = to_solve.split(maxsplit=1)
    nums = list(map(int, nums.split()))

    result = nums[0]
    for num in nums[1:]:
        result = operations[op](result, num)

    return result

def apply_to_each(func, iterable):
    return list(map(func, iterable))

def transform_lines(func, input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w',  encoding='utf-8') as outfile:
        for line in infile:
            transformed_line = func(line.strip())
            outfile.write(transformed_line + '\n')

if __name__ == '__main__':
    print(calc('+ 2 3'))

    print(calc_expand('+ 3 5 7 9'))
    print(calc_expand('/ 100 5 5 10'))

    print(apply_to_each(lambda x: x ** 2, [1, 2, 3, 4]))

    transform_lines(lambda x: x.upper(),'test_file.txt', 'transform_result.txt')