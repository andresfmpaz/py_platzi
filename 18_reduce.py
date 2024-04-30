import functools

numbers = [1, 2, 3, 4]

result = functools.reduce(lambda counter, item : counter + item, numbers)

print(result)

numbers_2 = [2, 4, 6, 8]

def acum(counter, item):
    print('counter -> ',counter)
    print('item -> ',item)
    return counter + item

result = functools.reduce(acum, numbers)



print(result)

def acum_1(counter, item):
    print('counter -> ',counter)
    print('item -> ',item)
    return counter - item

result = functools.reduce(acum_1, numbers)



print(result)