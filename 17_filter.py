# lets works with filters , filters are finctions that can get a small list from another bigger according with a condition
# lets see how filter works

numbers = [i for i in range(1,100)]
print('all numbers from 1 to 99 ',numbers)

#lets get a filter with even numbers

even_numbers = list(filter(lambda x: x % 2 == 0,numbers))

print('even numbers - > ', even_numbers)