a = int(input('Коэффициент a = '))
b = int(input('Коэффициент b = '))
c = int(input('Коэффициент c = '))
D = b*b - 4*a*c
if D >= 0:
    x1 = str((-b + D*0.5)/(2*a))
    x2 = str((-b - D*0.5)/(2*a))
    print('x1 = ' + x1, 'x2 = ' + x2)
else:
    print('Уровнение не имеет решения')
