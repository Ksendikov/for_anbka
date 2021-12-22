EXCHANGE_RATE = 25.5516
money_savings = float(input('Количесвто ваших сбережений = '))
number_of_dollars = int(money_savings / EXCHANGE_RATE)
print('Вы получите ' + str(number_of_dollars) + '$')