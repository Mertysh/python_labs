def pr(inp):
    try:
        fio, group, gpa = str(inp[0]).strip(), str(inp[1]), float(inp[2])
    except Exception as ex:
        return f'Данные введены в не верном формате ошибка {ex}'
    if 0 > gpa or gpa > 5: 
        return 'GPA в не верном формате'
    if fio == '' or len(fio.split()) < 2:
        return 'ФИО в не верном формате'
    if group == '':
        return 'Группа в не верном формате'

    inc = ''
    for n in fio.split()[1:3]:
        inc = inc + n[0].upper() + '.'
    name = fio.split()[0]
    inc = name[0].upper() + name[1:] + ' ' + inc
    return f'{inc}, гр. {group}, GPA {gpa:.2f}'

print(pr(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(pr(("Петров Пётр", "IKBO-12", 5.0)))
print(pr(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(pr(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(pr(("Петров", "IKBO-12", 5.0)))
print(pr(("Петров Пётр Петрович", "", 5.0)))
print(pr(("Петров Пётр Петрович", "IKBO-12", 7.0)))
print(pr(("Петров Пётр Петрович", "IKBO-12")))
