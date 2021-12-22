NUMBER_OF_APPLES_FOR_THE_PIE = 5
number_of_apples = input('Количество собранных яблок ')
number_of_pies = str(int(number_of_apples) // NUMBER_OF_APPLES_FOR_THE_PIE)
print('Количество пирогов = ' + number_of_pies)