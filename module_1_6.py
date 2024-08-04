my_dict = {'Fedor': 1975, 'Olga': 2012, 'Max': 1991, 'Alex': 1985}
print(my_dict)
print(my_dict['Olga'])
my_dict['Gleb'] = 2016
print(my_dict)
my_dict.update({'Klim': 2022, 'Sofiya': 2010})
print(my_dict)
del my_dict['Fedor']
print(my_dict.get('Fedor'))
print(my_dict)
my_set = {1, 3, 5, 7, 5, 3, 7, 1, 'volume', False, 3.145678, False, 'volume', 3.145678}
print(my_set)
my_set.add('month')
my_set.add(99)
my_set.discard(7)
print(my_set)
