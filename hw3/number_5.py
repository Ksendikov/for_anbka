EXCHANGE_RATE = 25.5516
DENOMINATION = 100
money_savings = float(input('Количесвто рублей = '))
number_of_dollars = int(money_savings / EXCHANGE_RATE)
number_of_denomination = number_of_dollars // DENOMINATION
amount_of_dollars_issued = number_of_denomination * DENOMINATION
print('Количесвто выданных доларов = ' + str(amount_of_dollars_issued))