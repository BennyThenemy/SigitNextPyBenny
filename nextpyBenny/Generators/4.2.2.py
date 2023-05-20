def parse_ranges(ranges_string):
    final_numbers_in_range_list = list()
    first_generator = ([int(num) for num in list_range.split("-")] for list_range in ranges_string.split(","))
    second_generator = ([num for num in range(int(start), int(stop)+1)] for start, stop in first_generator)
    for numbers_in_range_list in second_generator:
        final_numbers_in_range_list += numbers_in_range_list

    return final_numbers_in_range_list


def main():
    print(list(parse_ranges("1-2,4-4,8-10")))
    print(list(parse_ranges("0-0,4-8,20-21,43-45")))


if __name__ == '__main__':
    main()
