items = [
    {
        'product': 'shirt',
        'price': 100,
        'currency': 'usd',
    },
    {
        'product': 'short',
        'price': 55,
        'currency': 'usd'
    },
    {
        'product': 'gloves',
        'price': 15,
        'currency': 'usd'
    },
    {
        'product': 'scarf',
        'price': 12,
        'currency': 'usd'
    }
]

# now i want to create a list from dict structure but i want only the prices
# lets see how to build this list with map() function

prices = list(map(lambda item: item['price']+10, items))
print('new prices  ', prices)


new_items_v1 = list(map( lambda x: x|{'tax': x['price']*0.19} ,items)) 

print(items)
print(new_items_v1)

# lets add new element to each item
def add_taxes(item):
    item['taxes'] = item['price'] * 19
    return item

new_items = list(map(add_taxes,items))

print('new items with taxes ', new_items)

print('old items ', items)

print(items == new_items)

