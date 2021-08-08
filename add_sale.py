def main(argv):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        a = argv[1].split(',')
        a[0] = a[0].rjust(11, ' ')
        a[1] = a[1].ljust(2, '0')
        f.write(f'{",".join(a)}\n')


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
