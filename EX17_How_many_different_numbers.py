import re
import os

def how_many_didifferent_numbers(nums: list[int]) -> int:
    # # another way
    # unique_num = {*nums}
    # return len(unique_num)

    result = len(set(nums))
    return result

def get_unique_ips(log_file_path):
    unique_ips = set()
    with open(log_file_path, 'r') as file:
        for line in file:
            # Assuming the IP address is the first item in the log entry
            ip = line.split()[0]
            unique_ips.add(ip)
    return unique_ips


def get_response_codes(log_file_path):
    response_codes = set()
    with open(log_file_path, 'r') as file:
        for line in file:
            # Use regular expression to find the response code
            match = re.search(r'\d{3}', line)
            if match:
                response_codes.add(match.group())
    return response_codes


def get_file_extensions(directory):
    file_extensions = set()
    for filename in os.listdir(directory):
        _, extension = os.path.splitext(filename)
        if extension:  # Check if there is an extension
            file_extensions.add(extension)
    return file_extensions


if __name__ == '__main__':
    numbers = [1, 2, 3, 1, 2, 3, 4, 1]
    print(how_many_didifferent_numbers(numbers))

    # print("==========Beyond the exercise1==========")
    # # Example usage:
    # # Replace 'path_to_log_file' with the actual path to your log file
    # unique_ips = get_unique_ips('path_to_log_file')
    # print(unique_ips)

    # print("==========Beyond the exercise2==========")
    # # Example usage:
    # # Replace 'path_to_log_file' with the actual path to your log file
    # response_codes = get_response_codes('path_to_log_file')
    # print(response_codes)

    print("==========Beyond the exercise3==========")
    # Example usage:
    # Get file extensions in the current directory
    current_directory_extensions = get_file_extensions('.')
    print(current_directory_extensions)
    