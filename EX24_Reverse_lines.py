def reverse_lines(infilename, outfilename):
    with open(infilename, encoding='utf-8') as infile, open(outfilename, 'w', encoding='utf-8') as outfile:
        for one_line in infile:
            outfile.write(f'{one_line.rstrip()[::-1]}\n')

def encrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for char in infile.read():
            outfile.write(str(ord(char)) + ' ')

def decrypt_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            encrypted_chars = line.split()
            decrypted_chars = ''.join(chr(int(char)) for char in encrypted_chars)
            outfile.write(decrypted_chars)

def extract_vowels_consonants(input_file, vowels_file, consonants_file):
    vowels = 'aeiouAEIOU'
    with open(input_file, 'r', encoding='utf-8') as infile:
        with open(vowels_file, 'w', encoding='utf-8') as v_file, open(consonants_file, 'w', encoding='utf-8') as c_file:
            for line in infile:
                for char in line:
                    if char.isalpha():
                        if char in vowels:
                            v_file.write(char)
                        else:
                            c_file.write(char)

class MockPwd:
    def getpwall(self):
        # Mock data simulating /etc/passwd entries
        return [
            ('root', 'x', 0, 0, 'root', '/root', '/bin/bash'),
            ('daemon', 'x', 1, 1, 'daemon', '/usr/sbin', '/usr/sbin/nologin'),
            # Add more mock entries as needed
        ]

def list_users_by_shell(output_file):
    mock_pwd = MockPwd()

    shell_dict = {}
    for user in mock_pwd.getpwall():
        username = user[0]
        shell = user[6]
        if shell in shell_dict:
            shell_dict[shell].append(username)
        else:
            shell_dict[shell] = [username]

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for shell, users in shell_dict.items():
            outfile.write(f"{shell}:{', '.join(users)}\n")

if __name__ == '__main__':
    # reverse_lines('test_file.txt', 'reverse_test_file.txt')

    # Beyond the exercise1
    # encrypt_file('reverse_test_file.txt', 'encrypted.txt')
    # decrypt_file('encrypted.txt', 'decrypted.txt')

    # Beyond the exercise2
    # extract_vowels_consonants('test_file.txt', 'vowels.txt', 'consonants.txt')

    # Beyond the exercise3
    list_users_by_shell('users_by_shell.txt')