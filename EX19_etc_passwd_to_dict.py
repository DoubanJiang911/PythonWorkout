def passwd_to_dict(file_path: str) -> dict:
    user = {}
    with open(file_path, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                user[user_info[0]] = int(user_info[2])
    return user

def shells_to_dict(file_path: str) -> dict:
    shells = {}
    with open(file_path, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.strip().split(':')
                shells[user_info[-1]] = [user_info[0]]
    return shells

def factors_dict() -> dict:
    factors = {}
    user_input = input("Enter integers separated by spaces: ")
    nums = list(map(int, user_input.split(' ')))
    for num in nums:
        for factor in range(1, num + 1):
            if num % factor == 0:
                if factor in factors:
                    factors[factor].append(num)
                else:
                    factors[factor] = [num]
    return factors

def user_info_to_dict(file_path: str) -> dict:
    user = {}
    with open(file_path, 'r', encoding='utf-8') as passwd:
        for line in passwd:
            if not line.startswith(('#', '\n')):
                user_info = line.strip().split(':')
            user_name = user_info[0]
            user[user_name] = {'UserId': user_info[2], 'HomeDirectory': user_info[-2], 'Shell': user_info[-1]}
    return user

if __name__ == "__main__":
    print(passwd_to_dict('./etc/passwd'))

    print(shells_to_dict('./etc/passwd'))

    output_factors = factors_dict()
    for current_factor, multiples in output_factors.items():
        print(f"Factor: {current_factor}, Multiples: {multiples}")

    print(user_info_to_dict('./etc/passwd'))