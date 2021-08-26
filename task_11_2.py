class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num_1 = input('Введите делимое: ')
num_2 = input('Введите делитель: ')
try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_2 == 0:
        raise MyOwnErr('Делить на ноль нельзя')
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(round(num_1/num_2, 3))
