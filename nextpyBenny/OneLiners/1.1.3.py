def is_divided_by_four(n):
    return n % 4 == 0


def four_dividers(number):
    return list(filter(is_divided_by_four, range(1, number + 1)))


if __name__ == '__main__':
    print(four_dividers(9))
    print(four_dividers(3))
    