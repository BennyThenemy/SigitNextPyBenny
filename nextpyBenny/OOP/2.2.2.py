class Octopus:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age


def main():
    octopus1 = Octopus("Benny", 19)
    octopus2 = Octopus("Yossi", 21)

    octopus2.birthday()
    print(f"{octopus1.name}'s age: {octopus1.get_age()}")
    print(f"{octopus2.name}'s age: {octopus2.get_age()}")


if __name__ == '__main__':
    main()
