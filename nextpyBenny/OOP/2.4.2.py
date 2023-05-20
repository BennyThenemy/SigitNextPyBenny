class BigThing:
    def __init__(self, thing):
        self.thing = thing

    def size(self):
        if isinstance(self.thing, int):
            return self.thing
        return len(self.thing)


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super().__init__(thing)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "Ok"


def main():
    my_thing = BigThing("balloon")
    print(my_thing.size())

    cutie = BigCat("mitzy", 22)
    print(cutie.size())


if __name__ == '__main__':
    main()
