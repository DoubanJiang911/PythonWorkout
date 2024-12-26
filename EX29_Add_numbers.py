def add_numbers(input_str: str) -> int:
    return sum([int(s) for s in input_str.split() if s.isdigit()])

def filter_text(file_path):
    def filter_line(line):
        return len(line) > 20 and any(char in line for char in 'a e i o u'.split())
    return list(filter(filter_line, open(file_path, 'r', encoding='utf-8')))

def convert_phone_number(phone_list: list[str]) -> list[str]:
    output = []
    for phone in phone_list:
        current_start_with = phone.split('-')[0]
        first_phone_number = int(current_start_with[0])
        if first_phone_number in range(0,6):
            current_start_with = str(int(current_start_with) + 1)
            output.append(current_start_with + phone[3:])
        else:
            output.append(phone)
    return output

def change_area_code(phone_numbers):
    return [f"{int(code[:3])+1}-{code[3:7]}-{code[7:]}" if int(code[3:6]) < 600 else code for code in phone_numbers]

def convert_ages_to_months(people):
    return [
        {
            'name': p['name'],
            'age': p['age'],
            'age_in_months': p['age'] * 12
        }
        for p in people
        if p['age'] <= 20]

print(add_numbers("10 abc 20 de44 30 55fg 40"))

print(filter_text('test.txt'))

print(convert_phone_number(['123-456-7890', '520-333-4444', '099-777-8888']))

people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 15},
    {'name': 'Charlie', 'age': 20},
    {'name': 'David', 'age': 18},
    {'name': 'Eve', 'age': 22}
]
people_under_20 = convert_ages_to_months(people)
print(people_under_20)