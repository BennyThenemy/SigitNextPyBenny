def stop_iteration():
    iterable = iter([1, 2, 3])
    while True:
        print(next(iterable))


def zero_division_error():
    numerator = 10
    denominator = 0
    result = numerator / denominator
    print(result)


def assertion_error():
    x = 5
    y = 10
    assert x > y


"""
def import_error():
    import BennyTheKing
"""


def key_error():
    dictionary = {'key1': 'value1', 'key2': 'value2'}
    print(dictionary['key3'])


"""
def syntax_error():
    x = 5
    5 = x


def indentation_error():
    def inner_function():
    print("This line has incorrect indentation.")
"""


def type_error():
    numbers = [1, 2, 3, '4', 5]
    numbers_sum = 0
    for num in numbers:
        numbers_sum += num
    print(numbers_sum)


def main():
    """
    stop_iteration()
    zero_division_error()
    assertion_error()
    import_error()
    key_error()
    syntax_error()
    indentation_error()
    type_error()
    """


if __name__ == '__main__':
    main()
