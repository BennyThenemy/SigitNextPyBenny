import itertools


def main():

    bills = [20] * 3 + [10] * 5 + [5] * 2 + [1] * 5

    options = set()
    for r in range(1, len(bills) + 1):
        for combination in itertools.combinations(bills, r):
            if sum(combination) == 100:
                options.add(tuple(sorted(combination)))

    for option in options:
        print(option)

    print("Number of options:", len(options))


if __name__ == '__main__':
    main()
