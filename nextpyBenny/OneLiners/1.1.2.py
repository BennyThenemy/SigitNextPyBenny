def double_char(my_char):
    return my_char*2


def double_letter(my_str):
    return ''.join(list(map(double_char, my_str)))


if __name__ == '__main__':
    print(double_letter("python"))
    print(double_letter("we are the champions!"))
