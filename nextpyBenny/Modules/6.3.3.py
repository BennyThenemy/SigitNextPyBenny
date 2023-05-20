import pyttsx3


def main():
    engine = pyttsx3.init()
    engine.say("first time i'm using a package in next.py course")
    engine.runAndWait()


if __name__ == '__main__':
    main()
