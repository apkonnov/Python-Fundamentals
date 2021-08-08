from itertools import zip_longest
import json
with open('users.csv', 'r', encoding='utf-8') as f_users,\
        open('hobby.csv', 'r', encoding='utf-8') as f_hobby,\
        open('users_hobby.txt', 'w', encoding='utf-8') as f_users_hobby:
    users = f_users.readlines()
    hobby = f_hobby.readlines()
    if len(users) >= len(hobby):
        users = map(lambda el: el[:-1].replace(',', ' '), users)
        hobby = map(str.strip, hobby)
        users_hobby = dict(zip_longest(users, hobby))
        json.dump(users_hobby, f_users_hobby, ensure_ascii=False)
    else:
        exit(1)
