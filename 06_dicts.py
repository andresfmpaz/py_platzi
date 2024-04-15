import random

countries = {'col', 'mex', 'bol', 'pe'}

population_v2 = {country: random.randint(1, 500) for country in countries}

print(population_v2)

result = { country: population for (country, population) in population_v2.items() if population > 250}
print(result)    

text = "Hello , I am Andres, i learning python"
unique = { c: c.upper() for c in text if c in "aeiou"}
print(unique)
