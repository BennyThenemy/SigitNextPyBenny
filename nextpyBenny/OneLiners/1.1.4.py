from functools import reduce


def add(x, y):
    return x+y


def sum_of_digits(number):
    return int(reduce(add, list(map(int, str(number)))))


if __name__ == '__main__':
    print(sum_of_digits(104))