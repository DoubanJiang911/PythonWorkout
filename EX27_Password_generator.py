import random
import string

def create_password_generator(characters):
    def create_password(length):
        output = []
        for i in range(length):
            output.append(random.choice(characters))
        return ''.join(output)
    return create_password


def create_password_checker(min_uppercase, min_lowercase, min_punctuation, min_digits):
    def check_password(password):
        uppercase_count = sum(c in string.ascii_uppercase for c in password)
        lowercase_count = sum(c in string.ascii_lowercase for c in password)
        punctuation_count = sum(c in string.punctuation for c in password)
        digit_count = sum(c.isdigit() for c in password)

        return (uppercase_count >= min_uppercase and
                lowercase_count >= min_lowercase and
                punctuation_count >= min_punctuation and
                digit_count >= min_digits)

    return check_password

def getitem(key):
    def f(container):
        return container[key]
    return f

def doboth(f1, f2):
    def g(x):
        return f2(f1(x))
    return g

if __name__ == '__main__':
    alpha_password = create_password_generator('abcdef')
    symbol_password = create_password_generator('!@#$%')
    print(alpha_password(5))
    print(alpha_password(10))
    print(symbol_password(5))
    print(symbol_password(10))

    # Example usage:
    check_password = create_password_checker(1, 1, 1, 1)
    print(check_password("Aa1!"))
    print(check_password("Aa"))

    # Example usage:
    f = getitem('a')
    d = {'a': 1, 'b': 2}
    print(f(d))


    # Example usage:
    def square(x):
        return x * x

    def increment(x):
        return x + 1

    result_func = doboth(square, increment)
    print(result_func(2))  # Output: 5