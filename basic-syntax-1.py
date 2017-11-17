"""
Write a program that asks the user for a number (integer only) and prints the sum of its digits
"""


def get_input_from_user() -> int:
    while True:
        try:
            user_input = int(input('Podaj liczbę całkowitą: '))
        except ValueError:
            print('Błędny input, spróbuj jeszcze raz.')
        else:
            break
    return user_input


def sum_of_digits(num):
    return sum(map(int, str(num)))


def main():
    user_input = get_input_from_user()
    print(sum_of_digits(user_input))


if __name__ == '__main__':
    main()
