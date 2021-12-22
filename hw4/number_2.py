OFFICIAL_SALARY = 30000
salary = int(input('Сумма начисленной заработной платы = '))
if salary > OFFICIAL_SALARY:
    envelope_salary = str(salary - OFFICIAL_SALARY)
    print('Зарпалата в конверте ' + envelope_salary)
elif salary == OFFICIAL_SALARY:
    print('Вам не положено')
