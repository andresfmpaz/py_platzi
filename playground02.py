numbers = [35, 16 , 10 , 34, 37, 25]
even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)
even_numbers_v2 = [number for number in numbers if number % 2 == 0]
print(even_numbers_v2)