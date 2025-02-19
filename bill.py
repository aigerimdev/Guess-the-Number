# def calculate_and_display_bill(item_prices, sales_tax_rate):
#     # calculate subtotal
#     sub_total = 0
#     for price in item_prices:
#         sub_total += price

#     # add subtotal to calculate sales tax
#     sales_tax_total = sub_total * sales_tax_rate

#     # calculate grand total
#     grand_total = sub_total + sales_tax_total

#     # display totals
#     sub_total = f"${sub_total:.2f}"
#     sales_tax_total = f"${sales_tax_total:.2f}"
#     grand_total = f"${grand_total:.2f}"
    

#     return (f"""
#         **** Order Summary ****\n  
#         Item(s) Subtotal:  {sub_total}
#         Sales Tax:         {sales_tax_total}
#         --------------
#         Grand Total:       {grand_total}""")


# bill = calculate_and_display_bill([5.00, 8.00, 10.00], 0.08)
# print(bill)


# def calculate_subtotal(item_prices):
def calculate_total(flavor, milk, boba):
    # Prices for each option
    tea_prices = {
        'oolong': 4.50,
        'jasmine': 4.50,
        'silver needle': 5.00
    }
    
    milk_prices = {
        'none': 0.00,
        'dairy': 0.50,
        'oat': 0.75,
        'soy': 0.50
    }
    
    boba_prices = {
        'yes': 0.50,
        'no': 0.00
    }
    
    # Calculate total price
    total = tea_prices[flavor] + milk_prices[milk] + boba_prices[boba]
    
    return total


def drink_summary(flavor, milk, boba):
    total = calculate_total(flavor, milk, boba)

    print('*** Drink Summary ***')
    drink_display = flavor.capitalize()
    
    if milk != 'none' or boba != 'no':
        drink_display += ' with '
    
    if milk != 'none':
        drink_display += milk + ' milk'
    
    if milk != 'none' and boba != 'no':
        drink_display += ' and '
    
    if boba != 'no':
        drink_display += 'boba'
    
    print(drink_display)
    print(f'Drink total: ${total:.2f}')  # Formatting total to 2 decimal places


# Example Usage:
drink_summary('oolong', 'none', 'yes')
drink_summary('silver needle', 'oat', 'yes')
drink_summary('jasmine', 'dairy', 'no')