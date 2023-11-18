def split_and_join(line):
    # line="-".join(line.split(" "))
    return ("-".join(line.split(" ")))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line="this is okay ")
    print(result)
