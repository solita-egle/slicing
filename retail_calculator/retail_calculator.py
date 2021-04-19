UTAH = 6.85
NEVADA = 8
TEXAS = 6.25
ALABAMA = 4
CALIFORNIA = 8.25

TAX_RATES = {'UT': UTAH, 'NV': NEVADA, 'TX': TEXAS, 'AL': ALABAMA, 'CA': CALIFORNIA}


def get_order_value(nr_of_items: int, price: float, tax_rate: str):
    order_tax_rate = TAX_RATES.get(tax_rate) / 100
    plain_order_value = nr_of_items * price
    order_tax = order_tax_rate * plain_order_value
    order_value_with_tax = plain_order_value + order_tax
    discount_amount = get_discount(order_value_with_tax)
    print(discount_amount)
    #order_value = order_value_with_tax
    #return order_value


def get_discount(order_value: float):
    discount = 0
    if order_value >= 50000:
        discount = 15
    elif order_value >= 10000:
        discount = 10
    return discount


if __name__ == '__main__':
    get_order_value(2, 5000, 'AL')
