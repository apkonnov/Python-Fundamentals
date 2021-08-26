class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt

    @staticmethod
    def check_num(n):
        return n.replace('-', '', 1).replace('.', '', 1).isdigit()


result = []
while True:
    try:
        num = input('Введите число или stop: ')
        if num == 'stop':
            break
        if not MyOwnErr.check_num(num):
            raise MyOwnErr('Ошибка, введено не число!')
    except (ValueError, MyOwnErr) as err:
        print(err)
    else:
        result.append(float(num))
print(result)
