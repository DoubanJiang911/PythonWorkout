import re

def get_final_line(file_path: str) -> None:
    """以二进制模式读取文件，通过文件指针从文件末尾开始反向读取，同时通过buffer将读取内容写入缓存，直到遇见换行符或是到文件开头位置，最后反转输出buffer的内容"""
    with open(file_path, 'rb') as file:
        file.seek(0, 2)  # 将文件指针移动到文件的末尾
        position = file.tell()  # 获取文件末尾的位置
        buffer = bytearray()
        while position >= 0:
            file.seek(position - 1)
            next_byte = file.read(1)
            if not next_byte or next_byte == b'\n':  # 如果到达文件开头或遇到换行符
                if buffer:
                    break  # 使用一个循环向前读取字节，直到找到换行符或到达文件开头。将读取的字节存储在一个 bytearray 中
            buffer.append(next_byte[0])
            position -= 1
        print(buffer[::-1].decode('utf-8', errors='ignore').rstrip())  # 反转并解码为字符串

def sum_integer_words(file_path: str) -> int:
    total_sum = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            integer_words = re.findall(r'\b\d+\b', line)
            for word in integer_words:
                total_sum += int(word)
    return total_sum

def multiply_and_sum_columns(file_path: str) -> int:
    total_sum = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) == 2 and columns[0].isdigit() and columns[1].isdigit():
                total_sum += int(columns[0]) * int(columns[1])
    return total_sum

def count_vowels(file_path: str) -> dict:
    vowels = 'aeiou'
    vowel_count = {vowel: 0 for vowel in vowels}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for char in line:
                if char.lower() in vowels:
                    vowel_count[char.lower()] += 1
    return vowel_count

if __name__ == "__main__":
    get_final_line("test_file.txt")

    print("==========Beyond the exercise1==========")
    print(sum_integer_words("test_file.txt"))

    print("==========Beyond the exercise2==========")

    print("==========Beyond the exercise3==========")
    print(count_vowels("test_file.txt"))
    