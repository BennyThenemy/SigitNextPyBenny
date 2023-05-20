class UnderAge(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"your age ({self.arg}) is smaller than 18, wait {18 - int(self.arg)} years."


def send_invitation(name, age):
    try:
        if int(age) < 18:
            raise UnderAge(age)
    except UnderAge as e:
        print(e)
    else:
        print("You should send an invite to " + name)


def main():
    send_invitation("Benny", 20)
    send_invitation("Boss Baby", 17)


if __name__ == '__main__':
    main()
