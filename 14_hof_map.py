numbers = [1, 2, 3, 3, 4]
numbers_v2 = []

for number in numbers:
    numbers_v2.append(number * 2)
    
print(numbers)
print(numbers_v2)

numbers_v2_with_map = map(lambda number: number * 2, numbers)

print('result with map ', list(numbers_v2_with_map))

# lets see what happen with two list o more list

numbers_1 = [3, 6, 12, 24]
numbers_2 = [1, 2, 4]
numbers_3 = [1, 2, 3, 4, 5]

numbers_v3_with_map = map(lambda x, y, z: (x * y) - z, numbers_1, numbers_2, numbers_3 )

print(' x * y  - z  with map and lambda func ', list(numbers_v3_with_map))
