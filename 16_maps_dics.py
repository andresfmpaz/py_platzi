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

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = item['price'] * 19
    return new_item

new_items = list(map(add_taxes,items))

print('new items with taxes ', new_items)

print('old items ', items)
