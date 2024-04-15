numbers = []

for element in range(1, 11):
    numbers.append(element)

print(numbers)

numbers_v2 = [element * 2 for element in range(1 ,11)]
print('list comprehension: ', numbers_v2)
