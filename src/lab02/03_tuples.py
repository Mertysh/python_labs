def pr(inp):
    # Проверки ввода данных
    if not type(inp) is tuple:
        raise TypeError('Ввод должен быть кортежем')
    if len(inp) != 3:
        raise TypeError('В кортеже должно быть 3 элемента')

    fio, group, gpa = str(inp[0]).strip(), str(inp[1]), float(inp[2])
    
    if not type(gpa) is int and not type(gpa) is float:
        raise TypeError('GPA должно быть числом')
    if 0 > gpa or gpa > 5: 
        raise ValueError('GPA должно в диопозоне [0;5]')

    if not type(fio) is str:
        raise TypeError('ФИО должно быть строкой')
    if fio == '' or len(fio.split()) < 2:
        raise ValueError('ФИО в не верном формате')

    if not type(group) is str:
        raise TypeError('Группа должно быть строкой')
    if group == '':
        raise ValueError('Группа в не верном формате')

    # Преоброзование данных в нужный формат
    inc = ''
    for n in fio.split()[1:3]:
        inc = inc + n[0].upper() + '.'
    name = fio.split()[0]
    inc = name[0].upper() + name[1:] + ' ' + inc
    return f'{inc}, гр. {group}, GPA {gpa:.2f}'

# Тесты
test_cases = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6), 
    ("Петров Пётр", "IKBO-12", 5.0), 
    ("Петров Пётр Петрович", "IKBO-12", 5.0), 
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999), 
    ("Петров", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 7.0),
    ("Петров Пётр Петрович", "IKBO-12")
    ]
for case in test_cases:
    try: 
        print(f'{case} - {pr(case)}')
    except Exception as ex:
        print(f'{case} - {type(ex).__name__} {ex}')