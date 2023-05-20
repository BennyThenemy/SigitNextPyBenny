def read_file(file_name):
    context = "__CONTENT_START__"
    try:
        f = open(file_name)
    except IOError:
        context += "\n__NO_SUCH_FILE__"
    else:
        context += "\n" + f.readline()
        f.close()
    finally:
        context += "\n__CONTENT_END__"
        return context


def main():
    print(read_file("one_lined_file.txt")+"\n")
    print(read_file("file_does_not_exist.txt"))


if __name__ == '__main__':
    main()
