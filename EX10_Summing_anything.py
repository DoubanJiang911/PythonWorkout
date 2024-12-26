def mysum(*items):
    if not items:
        return items

    output = items[0]
    for item in items[1:]:
        output += item
    return output

def mysum_bigger_than(*items):
    if not items:
        return items

    length = len(items)
    if length == 1:
        return

    output = None
    for item in items[1:]:
        if item > items[0] and output is None:
            output = item
        elif item > items[0] and output is not None:
            output += item
        else:
            continue
    return output

def sum_numeric(*items):
    num = 0
    for item in items:
        if type(item) == int or item.isdigit():
            num += int(item)
    return num

def combine_dicts(list_of_dicts: list[dict]) -> dict:
    combined = {}
    for d in list_of_dicts:
        for key, value in d.items():
            if key in combined:
                if isinstance(combined[key], list):  # 指定键第三次及后续重复出现
                    combined[key].append(value)
                else:  # 指定键第二次出现
                    combined[key] = [combined[key], value]
            else:  # 指定键第一次出现
                combined[key] = value
    return combined


if __name__ == '__main__':
    print(mysum([]))
    print(mysum(10, 20, 30, 40))
    print(mysum('a', 'b', 'c', 'd'))
    print(mysum([10, 20, 30], [40, 50, 60], [70, 80]))

    print(mysum_bigger_than(10, 5, 20, 30, 6))
    print(mysum_bigger_than('b', 'a', 'c'))
    print(mysum_bigger_than())

    print(sum_numeric(10, 20, 'a', '30', 'bcd'))

    print(combine_dicts([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 5}]))