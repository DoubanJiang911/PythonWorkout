import os
import re
import hashlib
from arrow import Arrow

def find_longest_word(filename):
    longest_word = ''
    for one_line in open(filename, encoding='utf-8'):
        for one_word in one_line.split():
            if len(one_word) > len(longest_word):
                longest_word = one_word
                return longest_word

def find_all_longest_words(dirname):
    return {filename: find_longest_word(os.path.join(dirname, filename))
            for filename in os.listdir(dirname)
            if os.path.isfile(os.path.join(dirname, filename))}


def calculate_md5_hashes(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                md5_hash = hashlib.md5()
                while chunk := file.read(8192):
                    md5_hash.update(chunk)
                print(f"{filename}: {md5_hash.hexdigest()}")

def show_files_and_modification_time(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            modification_time = Arrow.fromtimestamp(os.stat(file_path).st_mtime).humanize()
            print(f"{filename}: Last modified {modification_time}")
    directory_modification_time = Arrow.fromtimestamp(os.stat(directory).st_mtime).humanize()
    print(f"Directory: Last modified {directory_modification_time}")

def summarize_http_requests(log_file_path):
    response_code_pattern = re.compile(r'\d{3}')
    request_count = 0

    with open(log_file_path, 'r') as file:
        for line in file:
            match = response_code_pattern.search(line)
            if match:
                request_count += 1

    print(f"Total requests resulting in numeric response codes: {request_count}")

if __name__ == '__main__':
    print(find_all_longest_words('.'))

    # print("==========Beyond the exercise1==========")
    # # Example usage:
    # calculate_md5_hashes('.')

    # print("==========Beyond the exercise2==========")
    # # Example usage:
    # show_files_and_modification_time('.')

    # print("==========Beyond the exercise3==========")
    # # Example usage:
    # # Replace 'path_to_log_file.log' with the actual path to your log file
    # summarize_http_requests('path_to_log_file.log')