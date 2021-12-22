input_string = input('Введите строку \n')
output_string = ''
for i in input_string:
    if i == 'р':
        output_string = output_string + 'л'
    else:
        output_string = output_string + i
print(output_string)
