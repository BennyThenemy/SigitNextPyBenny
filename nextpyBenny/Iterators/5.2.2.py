def main():
    numbers = iter(list(range(1, 101)))
    for i in numbers:
        next(numbers)
        next(numbers)
        next(numbers)
        print(i)


if __name__ == '__main__':
    main()
