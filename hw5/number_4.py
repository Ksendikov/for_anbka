first_number = int(input('Введите первое число '))
second_number = int(input('Введите второе число '))
count = 0
if first_number < second_number:
    for i in range(first_number, second_number + 1):
        if not i % 2 and not i % 5:
            count = count + 1
    print(count)
else:
    print('Второе число должно быть больше первого')

