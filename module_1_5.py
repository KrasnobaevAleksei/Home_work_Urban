immutable_var = (1, True, 'string')
print('Кортеж: \t\t\t', immutable_var)
#immutable_var[0] = 2
#нельзя изменить неизменяемый элемет Кортежа, можно поменять напимер список
mutable_list = [1, True, "string"]
mutable_list[2]= 'int'
print("Изменяемый список :\t", mutable_list)