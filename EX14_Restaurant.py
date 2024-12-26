from datetime import datetime, timedelta

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant(totally_cost: int):
    dish = input("Order: ").strip()
    price = MENU.get(dish)
    if not dish:
        print(f"Your total is {totally_cost}")
        return
    elif price:
        totally_cost += price
        print(f"{dish} costs {price}, total is {totally_cost}.")
        restaurant(totally_cost)
    else:
        print(f"Sorry, we are fresh out of {dish} today.")
        restaurant(totally_cost)


def login_system():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if user_database.get(username) == password:
        print("User has successfully logged in.")
    else:
        print("Access denied. Incorrect username or password.")

def temperature_lookup():
    date = input("Enter the date (YYYY-MM-DD): ").strip()
    if date in temperature_data:
        temp = temperature_data[date]
        print(f"The temperature on {date} was {temp} degrees.")

        date = datetime.strptime(date, "%Y-%m-%d")

        previous_day = date - timedelta(days=1)
        previous_day_str = previous_day.strftime("%Y-%m-%d")
        if previous_day_str in temperature_data:
            temp = temperature_data[previous_day_str]
            print(f"The temperature on {previous_day_str} was {temp} degrees.")

        next_day = date + timedelta(days=1)
        next_day_str = next_day.strftime("%Y-%m-%d")
        if next_day_str in temperature_data:
            temp = temperature_data[next_day_str]
            print(f"The temperature on {next_day_str} was {temp} degrees.")

def calculate_age():
    name = input("Enter the name of a family member: ")
    birth_date = family_birth_dates.get(name)

    if birth_date:
        today = datetime.today()
        #((today.month, today.day) < (birth_date.month, birth_date.day))计算天数，True则表示天数未满，则年龄计算结果-1
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        print(f"{name} is {age} years old.")
    else:
        print("Name not found in the family database.")

if __name__ == '__main__':
    restaurant(0)

    print("==========Beyond the exercise1==========")
    user_database = {
        'user1': 'password1',
        'user2': 'password2',
        'admin': 'secret'
    }
    login_system()

    print("==========Beyond the exercise2==========")
    temperature_data = {
        '2024-10-30': 130,
        '2024-10-31': 131,
        '2024-11-01': 1,
        '2024-11-09': 9,
        '2024-11-15': 10,
        '2024-11-16': 12,
        '2024-11-17': 15,
        '2024-11-18': 13,
        '2024-11-19': 11,
        '2024-11-20': 14,
        '2024-11-21': 16,
        '2024-11-31': 31,
    }
    temperature_lookup()

    print("==========Beyond the exercise3==========")
    family_birth_dates = {
        'Alice': datetime(1990, 5, 23),
        'Bob': datetime(1985, 10, 12),
        'Charlie': datetime(2005, 3, 9)
    }
    calculate_age()
