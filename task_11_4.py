class Warehouse:
    wh_list = []

    @staticmethod
    def check_num(n, m):
        if n.isdigit() and int(n) < int(m):
            return True
        else:
            return False

    def wh_menu(self):
        while True:
            menu_sel = input('Оргтехника: 1 - Добавить на склад  2 - Выдать со склада   '
                             '3 - Вернуть на склад  4 - Списать  0 - Выход\n')
            if menu_sel == '0':
                break
            elif self.check_num(menu_sel, 5):
                menu_sel = int(menu_sel)
                if menu_sel == 1:
                    self.wh_add()
                elif menu_sel == 2:
                    self.wh_give_out()
                elif menu_sel == 3:
                    self.wh_return()
                elif menu_sel == 4:
                    self.wh_del()
            else:
                print('Введите номер пункта меню')

    def wh_add(self):
        while True:
            sel = input('Что добавляем? 1 - Принтер, 2 - Сканер, 3 - Копир, 0 - Ничего\n')
            if sel == '0':
                break
            elif self.check_num(sel, 4):
                sel = int(sel)
                idx = len(self.wh_list)
                if sel == 1:
                    self.wh_list.append(Printer())
                    fl = '2'
                    while fl not in ('0', '1'):
                        fl = input('Тип принтера: 0 - струйный, 1 - лазерный ')
                    self.wh_list[idx].laser = True if fl == '1' else False
                elif sel == 2:
                    self.wh_list.append(Scanner())
                    fl = '2'
                    while fl not in ('0', '1'):
                        fl = input('Автоподача документов: 0 - нет, 1 - есть ')
                    self.wh_list[idx].auto_doc = True if fl == '1' else False
                elif sel == 3:
                    self.wh_list.append(Copier())
                    fl = '2'
                    while fl not in ('0', '1'):
                        fl = input('Тип копира: 0 - черно-белый, 1 - цветной1 ')
                    self.wh_list[idx].color = True if fl == '1' else False
                self.wh_list[idx].company = input('Производитель: ')
                self.wh_list[idx].model = input('Модель: ')
                self.wh_list[idx].format = 'A4'
                print('Добавлено на склад')
            else:
                print('Введите номер пункта меню')

    @staticmethod
    def wh_prn(wh_obj):
        wh_str = f'{wh_obj.type} {wh_obj.company} {wh_obj.model} ф.{wh_obj.format} '
        if wh_obj.type == 'Принтер':
            wh_str = wh_str + f'{"лазерный" if wh_obj.laser else "струйный"}'
        elif wh_obj.type == 'Сканер':
            wh_str = wh_str + f'{"с автоподачей" if wh_obj.auto_doc else "без автоподачи"}'
        elif wh_obj.type == 'Копир':
            wh_str = wh_str + f'{"цветной" if wh_obj.color else "черно-белый"}'
        wh_str = wh_str + f'   местоположение {wh_obj.division}'
        return wh_str

    def wh_give_out(self):
        for item in enumerate(self.wh_list, 1):
            if item[1].division == 'Склад':
                print(item[0], self.wh_prn(item[1]))
        while True:
            sel = input('Введите номер техники для выдачи (0 - Выход): ')
            if sel == '0':
                break
            elif self.check_num(sel, len(self.wh_list)+1):
                idx = int(sel)-1
                self.wh_list[idx].division = input('Подразделение: ')
                print('Выдано со склада')
            else:
                print('Нет такого номера')

    def wh_return(self):
        for item in enumerate(self.wh_list, 1):
            if item[1].division != 'Склад':
                print(item[0], self.wh_prn(item[1]))
        while True:
            sel = input('Введите номер техники для возврата (0 - Выход): ')
            if sel == '0':
                break
            elif self.check_num(sel, len(self.wh_list) + 1):
                idx = int(sel)-1
                self.wh_list[idx].division = 'Склад'
                print('Возвращено на склад')
            else:
                print('Нет такого номера')

    def wh_del(self):
        for item in enumerate(self.wh_list, 1):
            if item[1].division == 'Склад':
                print(item[0], self.wh_prn(item[1]))
        while True:
            sel = input('Введите номер техники для списания (0 - Выход): ')
            if sel == '0':
                break
            elif self.check_num(sel, len(self.wh_list)+1):
                idx = int(sel)-1
                self.wh_list.pop(idx)
                print('Списано')
            else:
                print('Нет такого номера')


class OfficeEquipment:
    type = 'Техника'
    company = ''
    model = ''
    format = 'A4'
    division = 'Склад'


class Printer(OfficeEquipment):
    type = 'Принтер'
    laser = True


class Scanner(OfficeEquipment):
    type = 'Сканер'
    auto_doc = False


class Copier(OfficeEquipment):
    type = 'Копир'
    color = False


wh_1 = Warehouse()

wh_1.wh_list.append(Printer())
wh_1.wh_list[0].company = 'HP'
wh_1.wh_list[0].model = 'LJ P1606'
wh_1.wh_list[0].format = 'A4'
wh_1.wh_list[0].laser = True

wh_1.wh_list.append(Printer())
wh_1.wh_list[1].company = 'Epson'
wh_1.wh_list[1].model = 'L1300'
wh_1.wh_list[1].format = 'A3'
wh_1.wh_list[1].laser = False

wh_1.wh_list.append(Scanner())
wh_1.wh_list[2].company = 'HP'
wh_1.wh_list[2].model = 'ScanJet Pro 2000'
wh_1.wh_list[2].format = 'A4'
wh_1.wh_list[2].auto_doc = True

wh_1.wh_list.append(Scanner())
wh_1.wh_list[3].company = 'Epson'
wh_1.wh_list[3].model = 'WorkForce DS-80W'
wh_1.wh_list[3].format = 'A4'
wh_1.wh_list[3].auto_doc = False

wh_1.wh_list.append(Copier())
wh_1.wh_list[4].company = 'Canon'
wh_1.wh_list[4].model = 'imageRUNNER 2206N'
wh_1.wh_list[4].format = 'A3'
wh_1.wh_list[4].color = False

wh_1.wh_list.append(Copier())
wh_1.wh_list[5].company = 'Canon'
wh_1.wh_list[5].model = 'imageRUNNER C3125i'
wh_1.wh_list[5].format = 'A3'
wh_1.wh_list[5].color = True

wh_1.wh_menu()
