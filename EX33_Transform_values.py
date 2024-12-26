def transform_values(func, a_dict):
    return {key: func(value)
            for key, value in a_dict.items()}

def temp_func(key, value) -> bool:
    if key in 'aeiou' or value % 2 == 0:
        return True
    else:
        return False

def expand_transform_values(func1, func2, a_dict):
    return {key: func1(value)
            for key, value in a_dict.items()
            if func2(key, value)}

def create_dict_by_username(passwd_path):
    return {line.split(':')[0]: int(line.split(':')[2])
            for line in open(passwd_path)
            if line[0] != '#'}

d = {'a':1, 'b':2, 'c':3}
print(transform_values(lambda x: x*x, d))
print(expand_transform_values(lambda x: x*x, temp_func, d))

print(create_dict_by_username('./etc/passwd'))