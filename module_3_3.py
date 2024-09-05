def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c= [1, 2, 3])
#2
list_ = [False, 99, 'third']
dict_ = {'a': True, 'b': 999, 'c': 'fourth'}
print_params(*list_)
print_params(**dict_)
#3
value_list = ['Five', 99]
print_params(*value_list, 42)