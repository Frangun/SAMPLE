from pyscript import display

# NOTES FROM EX2 -------------------------------

# first_name = 'Fran' # string
# last_name = 'Dela Cruz' 
# age = 15 # integer
# weight = '20.3' # float
# is_a_new_student = False
# sections = ['Emerald', 'Ruby', 'Topaz', 'Sapphire']

# display(first_name, target='div1')
# display(f'My name is {first_name} {last_name}! I am {age}, and I weigh {weight} kg', target='div1')
# display(f'I belong to 10 {sections[0]}', target='div1')

#SW2 -------------------------------------------

#String (displayed)
restaurant_name = 'Saja Snackrifice'

# String (displayed)
owner_name = 'Fran Ocean'

# Integer (displayed)
year_established = '2025'

# Integer
popular_item_price = '200'

# Boolean (displayed)
has_delivery = 'False'

# List
product_names = ['Saja Bowl', 'Soda pop-sicle', 'Saja Chips']

# Dictionary (displayed)
business_hours = {
    'Wednesday - Sunday': '9 am - 5 pm', 
    'Monday - Tuesday': 'closed'
}

# Dictionary
menu_prices = {
    'Saja Bowls': 200,
    'Soda pop-sicles': 30,
    'Saja Chips':15,
    'Soda gummies': 10,
    'Water': 10  
}

# String
common_allergens = ['Nuts', 'Dairy', 'Eggs']

# Float
tax_rate = 0.04

# Div1
display(restaurant_name, target='div1')
display(f'Est. {year_established}', target='div1')

# Div2
display(f'This current chain is owned by {owner_name} which is located in Makati, Legazpi Village. We serve rotating snacks (Limited Bowls, Chips, Candies) every week, leaving a special mark on time. Do we have delivery service? {has_delivery}! We want our customers to receive the full experience by paying us a visit to the actual place. Visit us now and get a chance to meet the members!', target='div2')

# Div4
display(f'Take note of our opening schedule from Wednesday to Sunday ( {business_hours['Wednesday - Sunday']} ) and Monday to Tuesday when we take breaks({business_hours['Monday - Tuesday']})', target='div4')

# display(f'I belong to 10 {sections[0]}', target='div1')
