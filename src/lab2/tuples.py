def pr(inp):
    fio, group, gpa = str(inp[0]), str(inp[1]), float(inp[2])
    inc = ''
    for n in fio.split()[1:3]:
        inc = inc + n[0].upper() + '.'
    name = fio.split()[0]
    inc = name[0].upper() + name[1:] + ' ' + inc
    print(f'{inc}, гр. {group}, GPA {gpa:.2f}')

pr(("Иванов Иван Иванович", "BIVT-25", 4.6))
pr(("Петров Пётр", "IKBO-12", 5.0))
pr(("Петров Пётр Петрович", "IKBO-12", 5.0))
pr(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))