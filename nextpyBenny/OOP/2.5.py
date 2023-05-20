class Animal:
    """
        Dog's, Cat's, Skunk's, Unicorn's and Dragon's super class.
    """
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger

    def get_name(self):
        return self._name

    def is_hungry(self):
        if self._hunger > 0:
            return True
        return False

    def feed(self):
        self._hunger -= 1

    def talk(self):
        # Implementing the functions in th subclass
        pass


class Dog(Animal):
    """
        Animal's sub class.
    """

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("woof woof")

    def feed(self):
        super().feed()
        self.talk()

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animal):
    """
        Animal's sub class.
    """

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("meow")

    def feed(self):
        super().feed()
        self.talk()

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    """
        Animal's sub class.
    """

    def __init__(self, name, hunger=0, stink_count=6):
        super().__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        print("tsssss")

    def feed(self):
        super().feed()
        self.talk()

    def stink(self):
        print("Dear lord!")


class Unicorn(Animal):
    """
        Animal's sub class.
    """

    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)

    def talk(self):
        print("Good day, darling")

    def feed(self):
        super().feed()
        self.talk()

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animal):
    """
        Animal's sub class.
    """

    def __init__(self, name, hunger=0, color="Green"):
        super().__init__(name, hunger)
        self._color = color

    def talk(self):
        print("Raaaawr")

    def feed(self):
        super().feed()
        self.talk()

    def breath_fire(self):
        print("$@#$#@$")


def main():

    # Creating animals objects:
    my_dog = Dog("Brownie", 10)
    my_cat = Cat("Zelda", 3)
    my_skunk = Skunk("Stinky")
    my_unicorn = Unicorn("Keith", 7)
    my_dragon = Dragon("Lizzy", 1450)

    new_dog = Dog("Doggo", 80)
    new_cat = Cat("Kitty", 80)
    new_skunk = Skunk("Stinky Jr.", 80)
    new_unicorn = Unicorn("Clair", 80)
    new_dragon = Dragon("McFly", 80)

    # list that contain all objects:
    zoo_lst = [my_dog, my_cat, my_dragon, my_unicorn, my_skunk,
               new_dog, new_cat, new_dragon, new_unicorn, new_skunk]

    # checking every animal in th list if hungry:
    for animal in zoo_lst:
        if animal.is_hungry():
            print(f"{str(type(animal).__name__)} {animal.get_name()}")

            # checking animals type and printing their catchphrase:
            if isinstance(animal, Dog):
                animal.fetch_stick()
            elif isinstance(animal, Cat):
                animal.chase_laser()
            elif isinstance(animal, Skunk):
                animal.stink()
            elif isinstance(animal, Unicorn):
                animal.sing()
            else:
                animal.breath_fire()

        # feeding the animal until they not hungry:
        while animal.is_hungry():
            animal.feed()

    # printing zoo's name:
    print(Animal.zoo_name)


if __name__ == '__main__':
    main()
