import my_functions 

def get_total(orders):
  #totals = get_total(orders)
  print(orders)
  totals = my_functions.get_total(orders)
  print(totals)
  return my_functions.calc_total(totals)

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)
