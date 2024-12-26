import shutil

def myxml(tagname, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"'
                     for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

def copyfile(input_file, *output_files):
    with open(input_file, 'rb') as f_in:
        for output_file in output_files:
            with open(output_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

def factorial(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

def anyjoin(sequence: iter, glue: any=' ') -> str:
    return glue.join(map(str, sequence))

if __name__ == '__main__':
    print(myxml('div', 'hello', a=1, b=2, c=3))

    # # Example usage:
    # copyfile('test_file.txt', 'copy1.txt', 'copy2.txt', 'copy3.txt')

    # Example usage:
    print(factorial(10, 2, 3, 4, 5))

    # Example usage:
    print(anyjoin([1, 2, 3]))
    print(anyjoin('abc', '**'))