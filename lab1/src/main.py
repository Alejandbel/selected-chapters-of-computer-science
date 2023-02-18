from hello import hello_world
from calculations import OPERATION, calculate


def main():
    hello_world()

    try:
        result = calculate(5, 6, OPERATION.MULT)
        print('Result of mult of 5 and 6:', result)
    except ZeroDivisionError:
        print('Error: division by zero')


if __name__ == '__main__':
    main()
