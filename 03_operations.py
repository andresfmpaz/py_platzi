set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

set_c = set_a.union(set_b)

print(set_c)

# se puede hacer union con un operador | 

print(set_a | set_b)


#ahora vamos con la interseccion

set_c = set_a.intersection(set_b)

print(set_c)

#usando operadores con conjuntos  &


print(set_a & set_b)

#operacio de diferencia de a - b
#quitamos los elementos de b en a

set_c = set_a.difference(set_b)
print('set a ', set_a)
print('set b ', set_b)
print('set a - set b',set_c)


# can be made by operators

print('set a - set b with operator (-)',set_a - set_b)

#lets make a symmetric difference it is all elements without intersection elements

set_c = set_a.symmetric_difference(set_b)

print('symmetric difference ', set_c)

#let use symmetric difference with (^) operator , lets see what's happen.. 

print('symmetric different with (^) set_a ^ set_b ', set_a ^ set_b)


