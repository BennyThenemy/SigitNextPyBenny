import winsound
from collections.abc import Iterable


def main():
    frequency_dic = {"la": 220,
                     "si": 247,
                     "do": 261,
                     "re": 293,
                     "mi": 329,
                     "fa": 349,
                     "sol": 392,
                     }

    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    version_1_notes_list = notes.split("-")
    notes_list = list()
    for notes in version_1_notes_list:
        notes_list.append(notes.split(","))

    print(f"is version_1_notes_list Iterable:  {isinstance(version_1_notes_list, Iterable)}")
    print(f"is notes_list Iterable:  {isinstance(notes_list, Iterable)}")

    iter_obj = iter(notes_list)
    while True:
        try:
            # Doing the beep beep beep:
            item = next(iter_obj)
            frequency = int(frequency_dic[item[0]])
            duration = int(item[1])
            winsound.Beep(frequency, duration)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
