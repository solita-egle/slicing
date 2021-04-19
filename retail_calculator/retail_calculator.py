UTAH = 6.85
NEVADA = 8
TEXAS = 6.25
ALABAMA = 4
CALIFORNIA = 8.25

TAX_RATES = {'UT': UTAH, 'NV': NEVADA, 'TX': TEXAS, 'AL': ALABAMA, 'CA': CALIFORNIA}


def get_order_value(nr_of_items: int, price: float, state_code: str):
    order_tax_rate = TAX_RATES.get(state_code.upper().strip()) / 100
    plain_order_value = nr_of_items * price
    order_tax = order_tax_rate * plain_order_value
    order_value_with_tax = plain_order_value + order_tax
    discount_amount = get_discount(order_value_with_tax)
    order_value = order_value_with_tax * (1 - discount_amount / 100)
    print(order_value)
    return order_value


def get_discount(order_value: float):
    discount = 0
    if order_value >= 50000:
        discount = 15
    elif order_value >= 10000:
        discount = 10
    elif order_value >= 7000:
        discount = 7
    elif order_value >= 1000:
        discount = 5
    return discount


def get_user_input():
    while True:
        try:
            nr_of_items = input('Please enter the nr of items: ')
        except ValueError:
            print('Wrong input. Please enter the number again')
            continue
        else:
            break
    while True:
        try:
            price = input('Please enter the price of an item: ')
        except ValueError:
            print('Wrong input. Please enter the number again')
            continue
        else:
            break
    while True:
        try:
            state_code = input('Please enter the state code: ')
        except ValueError:
            print('Wrong input. Please enter the state code again')
            continue
        else:
            break

def user_input_validation(nr_of_items,price,state_code):
    if not isinstance(nr_of_items, int):
        print("Value of number of items should be integer. Please enter the value again")
        return False
    if nr_of_items <= 0:
        print("Value of number of items should be greater than 0. Please enter the value again")
        return False
    

if __name__ == '__main__':
    user_input_validation('test', 51.15, 'UT')
