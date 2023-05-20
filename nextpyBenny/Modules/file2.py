"""
    file1.py, file2.py and main.py are ex 6.2.5:
"""

from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0):
        super().__init__()
        self._sender_age = sender_age

    def greeting_msg(self):
        super(BirthdayCard, self).greeting_msg()
        print(f"senders age: {self._sender_age}")
