def main():
    from sys import argv
    script, filename = argv
    filehand = open(filename)
    count = 0
    line = filehand.readline()
    words = len(line.split())
    chars = len(line)
    while line:
        count += 1
        line = filehand.readline()
        words += len(line.split())
        chars += len(line)
    print(f"{count} {words} {chars} {filename}")


main()
