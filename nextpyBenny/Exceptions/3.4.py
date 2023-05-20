import string

"""
    All exceptions are explained in the check_input function:
"""


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        illegal = ''.join(set(str(self.arg)).intersection(str(string.punctuation).replace('_', '')))
        return f'The username contains an illegal character "{illegal}" at index {str(self.arg).find(illegal)}'


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"The username is too short"


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"The password is missing a character"


class PasswordMissingCharacterUpperCase(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
        self.arg = arg

    def __str__(self):
        return f"{super().__str__()} (Uppercase)"


class PasswordMissingCharacterLowerCase(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
        self.arg = arg

    def __str__(self):
        return f"{super().__str__()} (Lowercase)"


class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
        self.arg = arg

    def __str__(self):
        return f"{super().__str__()} (Digit)"


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    def __init__(self, arg):
        super().__init__(arg)
        self.arg = arg

    def __str__(self):
        return f"{super().__str__()} (Special)"


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"The password is too short"


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self.arg = arg

    def __str__(self):
        return f"The password is too long"


def check_input(username, password):
    try:
        # Username contains illegal character like: "$","<",",","*","#"... (except: "_")
        if len(''.join(set(str(username)).intersection(str(string.punctuation).replace('_', '')))) > 0:
            raise UsernameContainsIllegalCharacter(username)
        # Username length shorter than 3
        elif len(str(username)) < 3:
            raise UsernameTooShort(username)
        # Username length longer than 16
        elif len(str(username)) > 16:
            raise UsernameTooLong(username)
        # Password length shorter than 8
        elif len(str(password)) < 8:
            raise PasswordTooShort(password)
        # Password length longer than 40
        elif len(str(password)) > 40:
            raise PasswordTooLong(password)
        # Password doesn't have upper characters
        elif not any(char.isupper() for char in password):
            raise PasswordMissingCharacterUpperCase(password)
        # Password doesn't have lower characters
        elif not any(char.islower() for char in password):
            raise PasswordMissingCharacterLowerCase(password)
        # Password doesn't have at least one digit
        elif not any(char.isdigit() for char in password):
            raise PasswordMissingCharacterDigit(password)
        # Password doesn't have lower special characters like: "$","<",",","*","#"...
        elif len("".join(c for c in str(password) if c not in string.punctuation)) == len(password):
            raise PasswordMissingCharacterSpecial(password)

    # Printing the Exceptions:
    except UsernameContainsIllegalCharacter as e:
        print(e)
    except UsernameTooShort as e:
        print(e)
    except UsernameTooLong as e:
        print(e)
    except PasswordMissingCharacter as e:
        print(e)
    except PasswordTooShort as e:
        print(e)
    except PasswordTooLong as e:
        print(e)
    # if the username and the password are good:
    else:
        print("OK")


def main():
    # inputs:
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6._1jk1mn0p")


if __name__ == '__main__':
    main()
