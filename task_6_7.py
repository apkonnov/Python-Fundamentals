def main(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        stop = f.tell()
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        len_str = 16
        start = int(argv[1]) - 1
        if len_str * start < stop:
            f.seek(len_str * start)
            a = argv[2].split(',')
            a[0] = a[0].rjust(11, ' ')
            a[1] = a[1].ljust(2, '0')
            f.write(f'{",".join(a)}\n')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
