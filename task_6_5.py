def main(argv):
    with open(sys.argv[1], 'r', encoding='utf-8') as f_users,\
         open(sys.argv[2], 'r', encoding='utf-8') as f_hobby,\
         open(sys.argv[3], 'w', encoding='utf-8') as f_users_hobby:
        len_users = sum(1 for _ in f_users)
        f_users.seek(0)
        len_hobby = sum(1 for _ in f_hobby)
        f_hobby.seek(0)
        if len_users >= len_hobby:
            for line in f_users:
                line_users = line.strip()
                line_hobby = f_hobby.readline()
                if len(line_hobby.strip()) < 1:
                    line_hobby = 'null\n'
                f_users_hobby.write(f'{line_users}: {line_hobby}')
            return 0
        else:
            return 1


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
