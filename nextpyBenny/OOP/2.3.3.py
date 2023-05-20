class Octopus:
    count_animals = 0

    def __init__(self, age, name="Octavio"):
        Octopus.count_animals += 1
        self._name = name
        self._age = age

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name


def main():
    octopus1 = Octopus(19, "Benny")
    octopus2 = Octopus(21,)

    print(f"{octopus1.get_name()}'s age: {octopus1.get_age()}")
    octopus1.set_name("Benjamin")
    print(f"{octopus1.get_name()}'s age: {octopus1.get_age()}")

    octopus2.birthday()
    print(f"{octopus2.get_name()}'s age: {octopus2.get_age()}")

    print(f"Animals number: {Octopus.count_animals}")


if __name__ == '__main__':
    main()
