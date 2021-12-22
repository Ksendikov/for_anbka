N = int(input('Количесвто купленных акций = '))
M = int(input('Стоимость одной акции =  '))
cost_of_shares = M * N
new_cost_one_shares = int(input('Новоя стоимость акции = '))
if new_cost_one_shares > M:
    new_cost_of_shares = new_cost_one_shares * N
    profit = str(new_cost_of_shares - cost_of_shares)
    print('Сумма выручки = ' + profit)
else:
    print('Not yet, John!')
