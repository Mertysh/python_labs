n = int(input('in_1: '))
ochn = 0
zaochn = 0
for i in range(2, n+2):
    second_name, name, age, status = input(f'in_{i}: ').split()
    if status == 'True': ochn += 1
    else: zaochn += 1
print(f'out: {ochn} {zaochn}')
