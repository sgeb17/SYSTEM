# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 21:46:01 2023

@author: BAD GAL RIRI
"""

# Discount list
discount = {'student': 0.2, 'senior': 0.3, 'pwd': 0.5}

# Delivery Charge
delivery_charge = 50

menu = {'a': {'name': 'Espresso', 'price': 80},
        'b': {'name': 'Americano', 'price': 100},
        'c': {'name': 'Latte', 'price': 120},
        'd': {'name': 'Mocha', 'price': 130},
        'e': {'name': 'Cappuccino', 'price': 110},
        'f': {'name': 'Bagel', 'price': 60}}

print("""
 ________            __     _ __          __    _    
/_  __/ /  ___   ___/ /__ _(_) /_ __  ___/ /___(_)__
 / / / _ \/ -_) / _  / _ `/ / / // / / _  / __/ / _ \\
/_/ /_//_/\__/  \_,_/\_,_/_/_/\_, /  \_,_/_/ /_/ .__/
                             /___/            /_/    
""")

print("                Rise, Sip & Grind                 ")

name = input("May I know your name please? ")
print("Hello, " + name + "! Here's our menu:")
print("--------------------")

def order():
    print("Welcome to the coffee shop!")
    name = input("May I know your name please? ")
    print("Hello, " + name + "! Here's our menu:")
    print("--------------------")
orders = {}

# Display menu
print("Menu:")
for key, value in menu.items():
    print(f"{key}. {value['name']}: {value['price']} pesos")

# Prompt user for input and quantity
selection = input("Enter the letter corresponding to your selection: ").lower()
quantity = int(input("Enter the quantity: "))

order_summary = []
# Get item name and price, and add to order summary
item_name = menu[selection]['name']
item_price = menu[selection]['price']
total_price = item_price * quantity
order_summary.append((item_name, quantity, item_price, total_price))


# Calculate total price
total_price = item_price * quantity

# Display selected item, quantity, price and total price
print(f"You selected {item_name} x {quantity} which costs {total_price} pesos.")


# User input for order selection
while True:
    item = input("Please enter your order (enter 'C' to checkout): ").lower()
    if item.upper() == 'C':
        break
    elif item in menu:
        quantity = int(input("Enter Quantity: "))
        orders[item] = quantity
        rder_summary = []
        # Get item name and price, and add to order summary
        item_name = menu[selection]['name']
        item_price = menu[selection]['price']
        total_price = item_price * quantity
        order_summary.append((item_name, quantity, item_price, total_price))

        # Calculate total price
        total_price = item_price * quantity

        # Display selected item, quantity, price and total price
        print(f"You selected {item_name} x {quantity} which costs {total_price} pesos.")

    else:
        print("Invalid item.")

# Bubble sort for ordering
print("Here's your order summary:")
print("Item\t\tQuantity\tPrice\t\tSubtotal")
print("-----------------------------------------------")
total = 0
for item in order_summary:
    item_name, quantity, item_price, total_price = item
    print(f"{item_name}\t\t\t{quantity}\t\t\t{item_price}\t\t\t{total_price}")
    total += total_price
print("-----------------------------------------------")
print(f"Total:\t\t\t\t\t\t{total}")



# User input for discount
discount_choice = input("Are you a student, senior citizen, or PWD? (y/n) ")
if discount_choice.lower() == 'y':
    discount_type = input("Please enter your discount type (Student/Senior/PWD): ").lower()
    if discount_type in discount:
        total = total * (1 - discount[discount_type])
        print("Discount applied! Your new total is: " + str(total))
    else:
        print("Invalid discount type.")

# User input for delivery
delivery_choice = input("Would you like to have it for pick up or delivery? (p/d) ")
if delivery_choice.lower() == 'd':
    address = input("Please enter your delivery address: ")
    print("Your address is,", address)
    total += delivery_charge
    print("Delivery charge applied. Your new total is: " + str(total))

# Payment system with multiple payment methods
print("Please choose your payment method:")
print("1. Cash")
print("2. Card")
print("3. GCash")
payment_choice = input("Enter the corresponding number: ")
if payment_choice == '1':
   cash = int(input("Enter cash amount: "))
   if cash >= total:
    change = cash - total
    print("Thank you for your payment! Your change is: " + str(change))
elif payment_choice == '2':
    card_number = input("Enter card number: ")
    expiry_date = input("Enter expiry date (mm/yy): ")
    cvv = input("Enter CVV: ")
    print("Thank you for your payment!")
elif payment_choice == '3':
    number = input("Enter your number: ")
    payment = input("Enter your payment: ")
    if payment == total:
        print("Successfully paid!")
    else:
        print("Try again!")
        print("Please choose your payment method:")
        print("1. Cash")
        print("2. Card")
        print("3. GCash")
        payment_choice = input("Enter the corresponding number: ")
        if payment_choice == '1':
            cash = int(input("Enter cash amount: "))
            if cash >= total:
                change = cash - total
                print("Thank you for your payment! Your change is: " + str(change))
        elif payment_choice == '2':
            card_number = input("Enter card number: ")
            expiry_date = input("Enter expiry date (mm/yy): ")
            cvv = input("Enter CVV: ")
            print("Thank you for your payment!")
        elif payment_choice == '3':
            number = input("Enter your number: ")
            payment = input("Enter your payment: ")
            if payment == total:
                print("Successfully paid!")
else:
    print("Invalid choice.")
# Confirmation of order
print("Thank you for ordering! Here's your receipt:")
print("---------------------------------------------")
print("Customer name: ", name)
print("----------------------------------------------")
print("Item : ", order_summary)
def order_again():               # Recursion method for ordering
    choice = input("Would you like to order again? (y/n) ")
    if choice.lower() == 'y':
        order()
    elif choice.lower() == 'n':
        print("Thank you for ordering!")
    else:
        print("Invalid choice.")
        order_again()





