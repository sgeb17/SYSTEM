# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:00:22 2023

@author: BAD GAL RIRI
"""
import sys

print("""
 ________            __     _ __          __    _    
/_  __/ /  ___   ___/ /__ _(_) /_ __  ___/ /___(_)__
 / / / _ \/ -_) / _  / _ `/ / / // / / _  / __/ / _ \\
/_/ /_//_/\__/  \_,_/\_,_/_/_/\_, /  \_,_/_/ /_/ .__/
                             /___/            /_/    
""")

print("                Rise, Sip & Grind                 ")



name = input("May I know your name please? :\t")
print("\n Hello, " + name + "! Here's our menu: \n")
print("--------------------")
        
def order():
      print("Welcome to the coffee shop!")
      name = input("May I know your name please? ")
      print("Hello, " + name + "! Here's our menu:")
      print("--------------------")


# Define menu and prices
menu = {'a': {'name': 'Espresso', 'price': 160},
        'b': {'name': 'Americano', 'price': 160},
        'c': {'name': 'Latte', 'price': 120},
        'd': {'name': 'Mocha', 'price': 140},
        'e': {'name': 'Cappuccino', 'price': 99},
        'f': {'name': 'Bagel', 'price': 60}}

# Initialize order summary list and orders dictionary
order_summary = []
orders = {}

# Display menu
print("Menu:")
for key, value in menu.items():
    print(f"{key}: {value['name']}: {value['price']} pesos")


# User input for order selection 
while True:
    item = input("Please enter your order (enter 'x' to checkout): ")
    if item == 'x':
        break
    elif item not in menu:
        print("That's not on the menu. Select another order")
    else:
        while True:
            quantity = input("How many? ")
            if quantity.isdigit():
                quantity = int(quantity)
                break
            else:
                print("Try Again. Enter a digit.")
        item_name = menu[item]['name']
        item_price = menu[item]['price']
        total_price = item_price * quantity
        orders[item] = quantity
        order_summary.append((item_name, quantity, item_price, total_price))
        print(f"You selected {item_name} x {quantity} which costs {total_price} pesos.")


# Calculate total price
total_price = sum([order[3] for order in order_summary])

# Display order summary and total price
print("\nOrder Summary:")
for orders in order_summary: 
    print(f"{orders[0]} x {orders[1]}: {orders[3]} pesos")
print(f"\nTotal Price: {total_price} pesos")    

 # Bubble sort for ordering
sorted_orders = sorted(orders.items(), key=lambda x: x[0])
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

# Discount list
discount = {'student': 0.2, 'senior': 0.3, 'pwd': 0.5}

# Delivery Charge
delivery_charge = 50

 # User input for discount
discount_choice = input("Are you a student, senior citizen, or PWD? (y/n) ") 
if discount_choice.lower() == 'y': 
    discount_type = input("Please enter your discount type (student/senior/pwd): ") 
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

#recursion method for ordering
def order_again():               
    choice = input("Would you like to order again? (y/n) ") 
    if choice.lower() == 'y': 
        order() 
    elif choice.lower() == 'n': 
        print("Alright then. Thanks for visiting the wesbite though.") 
        sys.exit
    else: 
        print("Invalid choice.") 
        order_again()
        
# Payment system with multiple payment methods 
print("Please choose your payment method:")
print("1. Cash")
print("2. Card")
payment_choice = input("Enter the corresponding number: ")
if payment_choice == '1': 
    cash = int(input("Enter cash amount: ")) 
    if cash >= total:
        change = cash - total
        print("Thank you for your payment! Your change is: " + str(change))
    else:
        print("Oops. Your Payment doesn't reach the Total Amount. Your order has been cancelled.")
        order_again()
elif payment_choice == '2': 
    card_number = input("Enter card number: ") 
    expiry_date = input("Enter expiry date (mm/yy): ")
    cvv = input("Enter CVV: ") 
    print("Thank you for your payment!") 
else: 
    print("Invalid choice. Your order has been cancelled.")
    order_again()

# Confirmation of order
print("Thank you for ordering! Here's your receipt:")
print("---------------------------------------------")   
print("Customer name: ", name)
print("----------------------------------------------") 
print("Item : ", order_summary) 

# Ask user if they want to order again
order_again()
