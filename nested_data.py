# Author: Paul A. Bloom
# dictionary inside a dictionary
# lists inside a dictionary
# dictionaries in a list
# lists in a list
# dictionary inside a list inside a dictionary

# HOW TO GET / UPDATE INFORMATION within nested data structures

# Shopping cart with lists inside a dictionary

cart = {
    'cleaning_products': ['soap', 'broom', 'shaving cream']
}

# print(cart)
# print(cart['cleaning_products'])

# print(type(cart['cleaning_products']))
# print(type(cart))

# print(cart['cleaning_products'][0])
# print(cart['cleaning_products'][1])

cart['cleaning_products'].append('mop')
cart['cleaning_products'].append('lysol')

#print(cart['cleaning_products'])

#print(cart)

# adding a new list as a value in a dictionary
cart['tooth_care'] = ['toothbrush', 'floss', 'mouthwash']

# remove floss (pop for a dictionary, but remove for a list)
cart['tooth_care'].remove('floss')

# use pop to remove the entire key-value pair for cleaning products
cart.pop('cleaning_products')

print(cart)

cart['home_improvement'] = {'shovel': 27.99,
                            'duct_tape': 2.17,
                            'paint': 17.43
                            }

print(cart)

print(cart['home_improvement']['shovel'])

# List: ORDERED  --- index
print(type(cart['tooth_care']))
print(cart['tooth_care'][1])

# Dictionary: NOT ORDERED -- key
print(type(cart['home_improvement']))
print(cart['home_improvement']['paint'])

cart['total_price'] = 28.99

a = []
b = {}

print(cart)

# another level of nesting

cart['tooth_care'].append({'floss': 2.39})

print(cart)
