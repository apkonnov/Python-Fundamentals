import re
RE_RAW = re.compile(r'([^ ]+)(.*\[)(.+)(] *")([A-Z]+)( *)([^ ]+)(.*" )(\d+)( *)(\d+)(.*)')
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    result = []
    for line in f:
        parsed_raw = RE_RAW.match(line).group(1, 3, 5, 7, 9, 11)
        result.append(parsed_raw)
    print(*result, sep=',\n')
