def join_numbers(numbers):
    return ','.join(str(number)
                    for number in numbers)

def int_to_string(numbers: list[int]) -> str:
    return ''.join(str(number)
                   for number in numbers
                   if number in range(0, 11))

def sum_hex_list(hex_str_list: list[str]) -> int:
    return sum([int(num)
                for hex_num in hex_str_list
                for num in hex_num
                if num.isdigit()])

def reverse_word(file_path):
    return [' '.join(line.split()[::-1]) for line in open(file_path, 'r', encoding='utf-8')]


print(join_numbers(range(15)))

num_list = [11,31,1,9,0,10,22]
print(int_to_string(num_list))

hex_list = [hex(num) for num in num_list]
print(sum_hex_list(hex_list))

print(reverse_word('test.txt'))

words = 'this is a bunch of words'.split()
def is_a_long_word(one_word):
    return len(one_word) > 4
x = filter(is_a_long_word, words)
print(' '.join(x))