my_dict={'Aleksei':1983, 'Anya':1991}
print('Dict: \t\t\t\t\t', my_dict)
print('Existing value: \t\t',my_dict.get('Aleksei'))
print('Not existing value: \t',my_dict.get('Kam'))
my_dict.update({'Sergei':1986, 'Anna':1984})
print('Deleted value: \t\t\t',my_dict.pop('Anna'))
print('Modified dictionary: \t',my_dict,'\n')

my_set={1,2,3,False,2,'motion',1,False}
print('Set: \t\t\t\t\t',my_set)
my_set.update({45,6})
my_set.remove(1)
print('Modified set: \t\t\t',my_set)
