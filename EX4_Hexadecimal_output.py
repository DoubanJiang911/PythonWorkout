def hex_output():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        decnum += int(digit, 16) * (16 ** power)
    print(decnum)


def to_int(base, num_str):
    base_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base > len(base_chars):
        raise ValueError("Base is too large for the character set")

    result = 0
    for char in num_str.upper():
        if char in base_chars:
            index = base_chars.index(char)
            if index >= base:
                raise ValueError(f"Character '{char}' is not legal for base {base}")
            result = result * base + index
        else:
            raise ValueError(f"Character '{char}' is not a valid digit in base {base}")

    return result

def print_name_triangle(name):
    for i in range(1, len(name) + 1):
        print(name[:i])

def hex_to_dec():
    decnum = 0
    hexnum = input('Enter a hex number to convert: ')
    for power, digit in enumerate(reversed(hexnum)):
        if digit.isdigit():
            decnum += (ord(digit) - 48) * (16 ** power)
        else:
            decnum += (ord(digit) - 55) * (16 ** power)
    print(decnum)

if __name__ == '__main__':
    # hex_output()

    # # Example usage:
    # print(to_int(10, "123"))  # Decimal number
    # print(to_int(16, "1A3"))  # Hexadecimal number
    #
    # # Ask the user for their name
    # user_name = input("Please enter your name: ")
    # print_name_triangle(user_name)

    hex_to_dec()