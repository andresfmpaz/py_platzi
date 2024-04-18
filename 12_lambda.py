
increment = lambda x : x + 1
print(increment(10))

full_name = lambda first_name, last_name : f'{first_name.title()} {last_name.title()}'

print(full_name('silvio', 'rodriguez'))

tuple_test = lambda number, string,  number2 : (number, string, number2, number+number2)

tp = tuple_test(22,'valores cualquiera', 33)
print(tp)
print(tp[0],tp[1])