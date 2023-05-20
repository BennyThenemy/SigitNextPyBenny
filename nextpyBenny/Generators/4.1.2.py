def translate(sentence):
    translated = ""
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translate_generator = (words[word] for word in sentence.split())
    for translation in translate_generator:
        translated += translation + " "
    return translated


def main():
    print(translate("el gato esta en la casa"))


if __name__ == '__main__':
    main()
