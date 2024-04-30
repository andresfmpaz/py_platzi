def get_total(orders):
    print(orders)
    totals = [order['total'] for order in orders]
    return totals

def calc_total(totals):
    return sum(totals)