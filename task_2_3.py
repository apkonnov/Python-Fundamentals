message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = ''
for mess in message:
    if mess.isdigit():
        result += f'"{int(mess):02}" '
    elif mess[1:].isdigit():
        result += f'"{mess[:1]}{int(mess[1:]):02}" '
    else:
        result += f'{mess} '
print(result)
