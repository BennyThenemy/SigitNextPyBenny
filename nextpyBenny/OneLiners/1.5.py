import functools


# converting the text to list and returning the list:
def make_text_to_list(file):
    with open(file, 'r') as file:
        return [line.strip() for line in file]


# returning longest name in list:
def longest_name(name_list):
    return max(name_list)


# char sum of all names in list:
def char_names_sum(name_list):
    return len(functools.reduce(lambda x, y: x + y, name_list))


# returning shortest name in list:
def shortest_name(name_list):
    return "\n".join(x for x in name_list if len(x) == len(min(names, key=len)))


# creating a file with length of each name:
def create_names_length(name_list):
    with open("name_length.txt", 'w') as name_length:
        name_length.write("\n".join(str(len(x)) for x in name_list))


# returning evey name with given length:
def get_name_with_length(name_list, length):
    return "\n".join(x for x in name_list if len(x) == int(length))


if __name__ == '__main__':
    names = make_text_to_list("names.txt")
    # 1:
    print(longest_name(names))
    # 2:
    print(char_names_sum(names))
    # 3:
    print(shortest_name(names))
    # 4:
    create_names_length(names)
    # 5:
    answer = input("Enter name length: ")
    print(get_name_with_length(names, answer))
