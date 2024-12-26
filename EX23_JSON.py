import json
import glob
import os
from datetime import datetime

def print_scores(dirname):
    scores = {}

    for filename in glob.glob(f'{dirname}/*.json'):
        scores[filename] = {}

        with open(filename) as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)

    for one_class in scores:
        print(one_class)
        for subject, subject_scores in scores[one_class].items():
            min_score = min(subject_scores)
            max_score = max(subject_scores)
            average_score = (sum(subject_scores) / len(subject_scores))

            print(subject)
            print(f'\tmin {min_score}')
            print(f'\tmax {max_score}')
            print(f'\taverage {average_score}')

# Mock pwd module
class MockPwd:
    def getpwall(self):
        # Mock data simulating /etc/passwd entries
        return [
            ('root', 'x', 0, 0, 'root', '/root', '/bin/bash'),
            ('daemon', 'x', 1, 1, 'daemon', '/usr/sbin', '/usr/sbin/nologin'),
            # Add more mock entries as needed
        ]

def passwd_to_json(output_file):
    mock_pwd = MockPwd()

    users = []
    for user in mock_pwd.getpwall():
        users.append(user)

    with open(output_file, 'w') as f:
        json.dump(users, f)

def passwd_to_dict_json(output_file):
    mock_pwd = MockPwd()

    users = []
    for user in mock_pwd.getpwall():
        users.append({
            'username': user[0],
            'password': user[1],
            'uid': user[2],
            'gid': user[3],
            'comment': user[4],
            'home_dir': user[5],
            'shell': user[6]
        })

    with open(output_file, 'w') as f:
        json.dump(users, f)


def directory_info_to_json(directory, output_file):
    files_info = []
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_stat = os.stat(file_path)
            files_info.append({
                'filename': filename,
                'size': file_stat.st_size,
                'last_modified': datetime.fromtimestamp(file_stat.st_mtime).isoformat()
            })

    with open(output_file, 'w') as f:
        json.dump(files_info, f)


def find_file_extremes(file_info_json):
    with open(file_info_json, 'r') as f:
        files_info = json.load(f)

    largest_file = max(files_info, key=lambda x: x['size'])
    smallest_file = min(files_info, key=lambda x: x['size'])
    most_recently_modified = max(files_info, key=lambda x: x['last_modified'])
    least_recently_modified = min(files_info, key=lambda x: x['last_modified'])

    print(f"Largest file: {largest_file['filename']} ({largest_file['size']} bytes)")
    print(f"Smallest file: {smallest_file['filename']} ({smallest_file['size']} bytes)")
    print(f"Most recently modified: {most_recently_modified['filename']} ({most_recently_modified['last_modified']})")
    print(
        f"Least recently modified: {least_recently_modified['filename']} ({least_recently_modified['last_modified']})")

if __name__ == '__main__':
    print_scores('.')

    # # Example usage:
    # passwd_to_json('passwd.json')

    # # Example usage:
    # passwd_to_dict_json('passwd_dict.json')

    # Example usage:
    directory = input("Enter the directory path: ")
    output_file = 'directory_info.json'
    directory_info_to_json(directory, output_file)
    find_file_extremes(output_file)