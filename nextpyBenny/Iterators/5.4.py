def check_id_valid(id_number):

    # if digit's index is even multiply it by 2 (if the length is bigger than 1 just add the two digits)
    # , otherwise multiply by 1.
    id_check = "".join(str(int(str(id_number)[x])*2 if len(str(int(str(id_number)[x])*2)) == 1
                           else str(int(str(int(str(id_number)[x])*2)[0]) + int(str(int(str(id_number)[x])*2)[1])))
                       if (x+1) % 2 == 0 else str(id_number)[x] for x in range(0, len(str(id_number))))

    # checking the sum of every digit
    id_check = sum(int(x) for x in id_check)
    return id_check % 10 == 0


class IDIterator:
    def __init__(self, given_id):
        self.id = int(given_id)

    def __iter__(self):
        return self

    def __next__(self):
        self.id = self.id + 1
        if self.id >= 999999999:
            raise StopIteration

        if check_id_valid(self.id):
            return self.id

        # if id not valid calling next iteration
        return self.__next__()


def id_generator(given_id):
    given_id += 1
    while given_id <= 999999999:
        if check_id_valid(given_id):
            yield given_id
        given_id += 1


def run_id_generator(given_id):
    index = 1
    for ig in id_generator(given_id):
        if index > 10:
            break
        print(ig)
        index += 1


def run_id_iterator(given_id):
    id_iterator = IDIterator(given_id)
    index = 1

    for id_t in id_iterator:
        if index > 10:
            break
        print(id_t)
        index += 1


def main():

    # print(check_id_valid(123456780))
    # print(check_id_valid(123456782))

    given_id = int(input("Enter ID: "))
    what_to_run = input("Generator or Iterator? (gen/it)?: ")

    if what_to_run == "gen":
        run_id_generator(given_id)
    elif what_to_run == "it":
        run_id_iterator(given_id)
    else:
        print(f"'{what_to_run}' is wrong input - gen / it")


if __name__ == '__main__':
    main()
