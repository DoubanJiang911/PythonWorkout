from decimal import Decimal, getcontext


def run_timing():
    """Asks the user repeatedly for numeric input. Prints the average time an
    d number of runs."""

    number_of_runs = total_time = 0
    print("Note: Press Enter to exit.")

    while True:
        n = input("Enter 10 km run time: ")
        if n == '':
            break

        try:
            n = float(n)
            total_time += n
            number_of_runs += 1
        except ValueError as e:
            print("This is not a valid number!")

    if number_of_runs:
        average_time = total_time / number_of_runs
        print(f"Average of {average_time:.1f}, over {number_of_runs} runs.")
    else:
        print("Average of 0, over 0 runs.")

def format_float(number, before, after):
    str_number = str(number)
    integer_part, decimal_part = str_number.split('.')
    formatted_integer = integer_part[-before:]
    formatted_decimal = decimal_part[:after]
    return float(f"{formatted_integer}.{formatted_decimal}")

def decimal_sum():
    getcontext().prec = 10

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    decimal1 = Decimal(num1)
    decimal2 = Decimal(num2)

    print(f"The sum of {decimal1} and {decimal2} is {decimal1 + decimal2}.")

if __name__ == "__main__":
    # run_timing()
    print(format_float(1234.5678, 2, 3))
    decimal_sum()