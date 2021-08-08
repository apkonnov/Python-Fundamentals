def main(argv):
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        len_str = 16
        if len(argv) > 2:
            start = int(argv[1])-1
            stop = int(argv[2])
            f.seek(len_str*start)
            for idx in range(start, stop):
                print(f.readline().strip())
        elif len(argv) > 1:
            start = int(argv[1])-1
            f.seek(len_str*start)
            for line in f:
                print(line.strip())
        else:
            for line in f:
                print(line.strip())


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
