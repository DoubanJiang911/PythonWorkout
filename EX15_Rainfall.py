import re

def get_rainfall():
    rainfall = {}
    while True:
        city_name = input("Enter city name: ")
        if not city_name:
            break

        mm_rain = input("Enter mm rain: ")
        if not mm_rain.isdigit():
            print("You must enter a valid number")
            continue

        if rainfall.get(city_name):
            rainfall[city_name] += int(mm_rain)
        else:
            rainfall[city_name] = int(mm_rain)

    for city, rain in rainfall.items():
        print(f"{city}: {rain}")

def calculate_rainfall():
    rainfall = {}
    while True:
        city_name = input("Enter city name: ")
        if not city_name:
            break

        mm_rain = input("Enter mm rain: ")
        if not mm_rain.isdigit():
            print("You must enter a valid number")
            continue

        if rainfall.get(city_name):
            rainfall[city_name].append(int(mm_rain))
        else:
            rainfall[city_name] = [int(mm_rain)]

    for city, rain in rainfall.items():
        print(f"city name: {city}, rain_total: {sum(rain)}, rain_avg: {sum(rain)/len(rain):.2f}")


def analyze_log_file(log_file_path):
    response_code_dict = {}
    pattern = r'(\d{3})\s+(\S+)'

    with open(log_file_path, 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                response_code = match.group(1)
                ip_address = match.group(2)
                if response_code not in response_code_dict:
                    response_code_dict[response_code] = []
                response_code_dict[response_code].append(ip_address)

    return response_code_dict

def count_word_lengths(file_path):
    word_length_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                length = len(word)
                if length > 0:
                    word_length_dict[length] = word_length_dict.get(length, 0) + 1
    return word_length_dict


if __name__ == '__main__':
    get_rainfall()

    print("==========Beyond the exercise1==========")
    calculate_rainfall()

    # print("==========Beyond the exercise2==========")
    # Example usage:
    # Replace 'path_to_log_file' with the actual path to your log file
    # log_data = analyze_log_file('path_to_log_file')
    # for code, ips in log_data.items():
    #     print(f"Response Code {code}: {ips}")

    # print("==========Beyond the exercise3==========")
    # Example usage:
    # Replace 'path_to_text_file' with the actual path to your text file
    # word_lengths = count_word_lengths('path_to_text_file')
    # for length, count in sorted(word_lengths.items()):
    #     print(f"Words of length {length}: {count}")