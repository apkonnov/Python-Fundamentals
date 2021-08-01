from requests import get, utils


def currency_rates(curr_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    idx = content.find(curr_code.upper())
    if idx > 0:
        curr_val = content[content.find('<Value>', idx) + 7:content.find('</Value>', idx)]
        return float(curr_val.replace(',', '.'))
    else:
        return None


print(currency_rates('Usd'))
print(currency_rates('EUR'))
