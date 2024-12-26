from operator import itemgetter

PEOPLE = [
    {
        'first':'Reuven', 'last':'Lerner',
        'email':'reuven@lerner.co.il'
    },
    {
        'first':'Donald',
        'last':'Trump',
        'email':'president@whitehouse.gov'
    },
    {
        'first':'Vladimir',
        'last':'Putin',
        'email':'president@kremvax.ru'
    }
]

# def alphabetize_names():
#     persons = sorted(PEOPLE, key=lambda x: (x['last'], x['first']))
#     for person in persons:
#         print(f'{person["last"]}, {person["first"]}: {person["email"]}')

def alphabetize_names(list_of_dicts):
    return sorted(list_of_dicts,
                  key=itemgetter('last', 'first'))

def sort_by_absolute_value(sequence: iter):
    return sorted(sequence, key=lambda x: abs(x))

def sort_by_vowels_count(list_of_strings: list[str]) -> list[str]:
    vowels = 'aeiou'
    list_of_strings = set(list_of_strings)  # 去重
    output_list = []
    for word in list_of_strings:
        temp_dict = {}  # 字符串和元音次数，组合成为字典写入列表
        vowels_sum = 0  # 统计元音次数
        for letter in word.lower():
            if letter in vowels:
                vowels_sum += 1
        temp_dict['name'] = word
        temp_dict['num'] = vowels_sum
        output_list.append(temp_dict)
    # 将列表中的字典按照num统计次数倒序排序
    sorted_words = sorted(output_list, key=lambda x:x['num'], reverse=True)
    # 仅返回列表中字典的name字段
    return list(map(itemgetter('name'), sorted_words))

def sort_by_sum_of_list(num_list: list[list]) -> list[list]:
    output_list = []
    for inner_list in num_list:
        temp_dict = {'list': inner_list, 'sum': sum(inner_list)}
        output_list.append(temp_dict)
    sorted_list = sorted(output_list, key=lambda x:x['sum'], reverse=True)
    return list(map(itemgetter('list'), sorted_list))


if __name__ == "__main__":
    # alphabetize_names()
    print(alphabetize_names(PEOPLE))

    print(sort_by_absolute_value([7,8,9,-4,-5,-6]))

    print(sort_by_vowels_count(['hello', 'world', 'algorithm', 'python', 'exercise']))

    print(sort_by_sum_of_list([[4,5,6],[],[1,10,2,3],[9,8,7]]))