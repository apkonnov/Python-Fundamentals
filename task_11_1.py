import datetime
import re


class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract(cls, d_str):
        re_date = re.compile(r'^(\d{2}[./-]){2}\d{4}$')
        valid_str = re_date.match(d_str)
        if valid_str:
            day = int(valid_str.group()[:2])
            month = int(valid_str.group()[3:5])
            year = int(valid_str.group()[6:10])
            if Date.validation(day, month, year):
                result = (day, month, year)
                return result
            else:
                return 'Нет такой даты'
        else:
            return 'Неверный формат даты'

    @staticmethod
    def validation(d, m, y):
        try:
            datetime.date(y, m, d)
            return True
        except ValueError:
            return False


date_1 = Date('24.08.2021')
date_2 = Date('24.8.2021')
date_3 = Date('24-13-2021')
print(Date.extract(date_1.date_str))
print(Date.extract(date_2.date_str))
print(Date.extract(date_3.date_str))
