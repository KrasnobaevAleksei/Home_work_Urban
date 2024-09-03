calls = 0
def counts_call():
    global calls
    calls += 1
    return calls
def string_info(stroka):
     counts_call()
     tuple_ =(len(stroka), stroka.lower(), stroka.upper())
     return tuple_
def is_contains(str_2, list_):
    counts_call()
    for i  in list_:
        if i == str_2:
            check = True
            break
        else:
            check = False
    return check
print(string_info('Привет !'))
print(string_info('Пока !'))
print(is_contains('Hello',[2, 'Hello', 1, 'Привет' ]))
print(is_contains('Hello',['Пока', 1, 'Привет' ]))
print('Итого получилось: ', calls)