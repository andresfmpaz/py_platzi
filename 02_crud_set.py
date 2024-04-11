set_countries = {'col','mex','bol'}

size = len(set_countries)
print(f' el tamano es {size}')

print('col' in set_countries)

print('pe' in set_countries)

print(set_countries.add('pe'))
print(set_countries)
print('peru esta en el conjunto ', 'pe' in set_countries)
print('antes update',set_countries)
#actualizar un conjunto con update
set_countries.update({'arg', 'bol', 'urg', 'cl'})
set_countries_all = set_countries.update({'arg', 'bol', 'urg', 'cl'})
print('despues update',set_countries)

#print('remove ',set_countries.remove('ar'))
print('discard ',set_countries.discard('arg'))
print('despues del discard',set_countries)

print('union',set_countries_all)
