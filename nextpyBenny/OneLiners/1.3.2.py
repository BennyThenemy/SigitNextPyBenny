def is_prime(number):
    return all(number % i != 0 for i in range(2, number)) if number > 1 else False


if __name__ == '__main__':
    print(is_prime(42))
    print(is_prime(43))
