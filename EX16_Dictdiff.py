def dictdiff(first: dict, second: dict) -> dict:
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first.get(key) != second.get(key):
            output[key] = [first.get(key), second.get(key)]

    return output

def merge_dicts(*dicts: dict) -> dict:
    result = {}
    for d in dicts:
        result.update(d)
    return result

def create_dict_from_args(*args) -> dict:
    if len(args) % 2 != 0:
        raise ValueError("Arguments must be in pairs (keys and values)")
    return dict(zip(args[::2], args[1::2]))

def dict_partition(d: dict, f) -> tuple[dict, dict]:
    true_dict = {}
    false_dict = {}
    for key, value in d.items():
        if f(key, value):
            true_dict[key] = value
        else:
            false_dict[key] = value
    return true_dict, false_dict

if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'd': 3}
    d2 = {'a': 1, 'b': 2, 'c': 4}
    print(dictdiff(d1, d2))

    print("==========Beyond the exercise1==========")
    d3 = {'a': 9, 'b': 8, 'c': 7}
    d4 = {'a': 4, 'e': 5, 'f': 6}
    print(merge_dicts(d1, d2, d3, d4))

    print("==========Beyond the exercise2==========")
    print(create_dict_from_args('a', 1, 'b', 2, 'd', 3, 'a', 1, 'b', 2, 'c', 4, 'a', 9, 'b', 8, 'c', 7, 'a', 4, 'e', 5, 'f', 6))

    print("==========Beyond the exercise3==========")
    data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    even_values, odd_values = dict_partition(data, lambda k, v: v % 2 == 0)
    print(even_values)
    print(odd_values)