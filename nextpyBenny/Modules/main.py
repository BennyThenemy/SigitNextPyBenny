"""
    file1.py, file2.py and main.py are ex 6.2.5:
"""

from file1 import GreetingCard
from file2 import BirthdayCard


def main():
    gc = GreetingCard()
    bc = BirthdayCard()
    gc.greeting_msg()
    bc.greeting_msg()


if __name__ == '__main__':
    main()
