class MusicNotes:
    def __init__(self):
        self.oct_list = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        self.index = -1
        self.oct_mul = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= int(len(self.oct_list)-1):
            if self.oct_mul >= 16:
                raise StopIteration()

            self.index = -1
            self.oct_mul = self.oct_mul * 2

        self.index += 1
        return self.oct_list[self.index] * self.oct_mul


def main():
    notes_iter = iter(MusicNotes())
    for freq in notes_iter:
        print(freq)


if __name__ == '__main__':
    main()
