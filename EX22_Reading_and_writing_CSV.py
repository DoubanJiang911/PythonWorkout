import csv
import random

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as passwd, open(csv_filename, 'w') as output:
        infile = csv.reader(passwd, delimiter=':')
        outfile = csv.writer(output, delimiter='\t')
        for record in infile:
            if len(record) > 1:
                outfile.writerow((record[0], record[2]))

def write_custom_fields_delimiter():
    fields = input("Enter space-separated field indices (1-indexed): ")
    delimiter = input("Enter delimiter character: ")
    output_file = "custom_passwd.csv"

    field_indices = [int(f) - 1 for f in fields.split()]

    with open('./etc/passwd', 'r') as passwd_file, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(passwd_file)
        writer = csv.writer(output_csv, delimiter=delimiter)

        for row in reader:
            custom_row = [row[i] for i in field_indices]
            writer.writerow(custom_row)

def write_dict_to_csv(dict_data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key, value in dict_data.items():
            writer.writerow([key, value, type(value).__name__])

def create_random_integers_csv(output_file, lines=10, num_per_line=10, start=10, end=100):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for _ in range(lines):
            row = [random.randint(start, end) for _ in range(num_per_line)]
            writer.writerow(row)

def read_and_calculate_statistics(input_file):
    total_sum = 0
    count = 0
    with open(input_file, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            line_sum = sum(map(int, row))
            total_sum += line_sum
            count += 1
            mean = line_sum / len(row)
            print(f"Sum: {line_sum}, Mean: {mean}")
    overall_mean = total_sum / count
    print(f"Overall Mean: {overall_mean}")

if __name__ == '__main__':
    # # Example usage:
    # write_custom_fields_delimiter()

    # # Example usage:
    # data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    # write_dict_to_csv(data, 'dict_data.csv')

    # Example usage:
    output_file = 'random_integers.csv'
    create_random_integers_csv(output_file)
    read_and_calculate_statistics(output_file)