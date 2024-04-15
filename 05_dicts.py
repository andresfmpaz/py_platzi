import random

# following you can see how to create a dict with a for

dict = {}

for i in range(1, 11):
    dict[i] = i * 2
# here you can realize the dict with a key and value


print(dict)
# something like : {1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20}

# following you can see how to create a dict using dict comprehension
dict_v2 = {i: i * 2 for i in range(1, 11)}
# The result is the same just in one line
print(dict_v2)

# Let's make it different

countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 5000)
# The result is similar to {'col': 2287, 'mex': 2991, 'bol': 2445, 'pe': 1436}
# remember , the numbers will change every time the code is executed!!
print(population)
# It country from countries will be the dict key and the value come from random.ranint() 
population_v2 = {country: random.randint(1, 5000) for country in countries}
print(population_v2)
