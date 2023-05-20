"""
    file1.py, file2.py and main.py are ex 6.2.5:
"""


class GreetingCard:
    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f"sender: {self._sender}, recipient: {self._recipient}")

    # Importing this code to file2.py
