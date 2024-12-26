import random


def guessing_game():
    number = random.randint(0, 100)
    cnt = 0

    while True:
        guess_num = input("Enter a guess between 0 and 100: ")

        try:
            guess_num = int(guess_num)
        except ValueError as e:
            print("Must enter a number, only int type.")
            continue

        cnt += 1
        if guess_num > number:
            print("Too high, guess again.")
        elif guess_num < number:
            print("Too low, guess again.")
        else:
            print(f"Just right, you guessed {cnt} times, game end.")
            return 0


if __name__ == '__main__':
    guessing_game()