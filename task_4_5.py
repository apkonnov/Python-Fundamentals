from requests import get, utils
from datetime import datetime


def currency_rates(curr_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    date_str = content[content.find('Date=') + 6:content.find('Date=') + 16]
    idx = content.find(curr_code.upper())
    if idx > 0:
        curr_val = content[content.find('<Value>', idx) + 7:content.find('</Value>', idx)]
        print(datetime.strptime(date_str, '%d.%m.%Y').date(), end=', ')
        return float(curr_val.replace(',', '.'))
    else:
        return None


if __name__ == "__main__":
    from sys import argv
    args = argv[1:]
    print(currency_rates(args[0]))
