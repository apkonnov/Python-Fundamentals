message = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
for idx, mess in enumerate(message):
    if mess.isdigit():
        message[idx] = f'"{int(mess):02}"'
    elif mess[1:].isdigit():
        message[idx] = f'"{mess[:1]}{int(mess[1:]):02}"'
print(' '.join(message))
