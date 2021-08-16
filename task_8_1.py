# Допустимо использовать в имени пользователя только латинские буквы, цифры, знак подчеркивания, точку и минус
# имя пользователя начинается с буквы или цифры

import re
RE_EMAIL = re.compile(r'^(?P<username>[a-z0-9][a-z0-9._-]+)@(?P<domain>[a-z0-9]+\.[a-z]{2,4})$')


def email_parse(email_address):
    if RE_EMAIL.match(email_address):
        return RE_EMAIL.match(email_address).groupdict()


if __name__ == '__main__':
    try:
        email = input('Введите email: ')
        valid_email = email_parse(email.lower())
        if valid_email:
            print(f'имя пользователя: {valid_email.get("username")}')
            print(f'почтовый домен: {valid_email.get("domain")}')
        else:
            raise ValueError(f'ValueError: wrong email: {email}')
    except ValueError as e:
        print(f'Еrr: {e}')
