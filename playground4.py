def multiply_numbers(numbers):
    # Escribe tu solución 👇
    numbers_v2 = list(map(lambda x: x * 2, numbers))
    return numbers_v2

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)

numbers = [2, 4, 5, 6, 8]

response = multiply_numbers(numbers)
print(response)

numbers = [1, 1, -2, -3]

response = multiply_numbers(numbers)
print(response)