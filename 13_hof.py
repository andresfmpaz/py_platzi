
def increment(x):
    return x + 1

def high_order_function(x,func):
    return x + func(x)

result = high_order_function(33,increment)

print(' normal function ', result)


increment_v2 = lambda x : x + 2
high_order_func_v2 = lambda x, func: x + func(x)

result = high_order_func_v2(10, increment_v2)

print('lambda1 ', result)

result = high_order_func_v2(10, lambda x: x * 2)

print('lambda2 ', result)

hof_3 = lambda x , y , func : x + ' ' + y +'  function value  - > '+func(x, y)

result = hof_3('sivio', 'rodriguez', lambda x, y : x.upper()+ ' ' + y.upper())

print('hof with text  ', result)