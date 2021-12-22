number_of_colleagues = int(input('Количесвто сотрудников компании = '))
count = 0
for i in range(number_of_colleagues):
    colleagues_age = input('Возраст сотрудника ' + str(i+1) + ' ')
    if not int(colleagues_age) % 5:
        count = count + 1
print(count)
