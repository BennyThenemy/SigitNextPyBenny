def is_funny(string):
    return all(c == 'h' or c == 'a' for c in string)


if __name__ == '__main__':
    print(is_funny("hahahahahaha"))