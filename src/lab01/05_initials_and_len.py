name = input('ФИО: ')
inc = ''
for n in name.split():
    inc = inc + n[0].upper()
print(f'Инициалы: {inc}.')
print(f'Длина (символов): {len(name.replace(' ', ''))+2}')