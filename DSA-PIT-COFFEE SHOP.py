# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 23:00:22 2023

@author: BAD GAL RIRI
"""


print("""
 ________            __     _ __          __    _    
/_  __/ /  ___   ___/ /__ _(_) /_ __  ___/ /___(_)__
 / / / _ \/ -_) / _  / _ `/ / / // / / _  / __/ / _ \\
/_/ /_//_/\__/  \_,_/\_,_/_/_/\_, /  \_,_/_/ /_/ .__/
                             /___/            /_/    
""")

print("                Rise, Sip & Grind                 ")

import sys
import datetime

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
# Sort the order summary by item name
for i in range(len(order_summary)):
    for j in range(len(order_summary) - 1 - i):
        if order_summary[j][0] > order_summary[j + 1][0]:
            order_summary[j], order_summary[j + 1] = order_summary[j + 1], order_summary[j]

# Print the sorted order summary
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
print("2. Credit Card")
print("3. Debit Card")
print("4. GCash")
payment_choice = input("Enter the corresponding number: ")
if payment_choice == '1': 
    cash = int(input("Enter cash amount: ")) 
    if cash >= total:
        change = cash - total
        print("Thank you for your payment! Your change is: " + str(change))
    else:
        print("Oops. Your payment doesn't reach the total amount. Your order has been cancelled.")
        order_again()
elif payment_choice == '2': 
    card_number = input("Enter credit card number (16 digits): ")
    if len(card_number) != 16 or not card_number.isdigit():
        print("Invalid credit card number.")
        order_again()
    expiry_date = input("Enter expiry date (mm/yy): ")
    cvv = input("Enter CVV (3 digits): ") 
    if len(cvv) != 3 or not cvv.isdigit():
        print("Invalid CVV.")
        order_again()
    print("Thank you for your payment!") 
elif payment_choice == '3': 
    card_number = input("Enter debit card number (16 digits): ")
    if len(card_number) != 16 or not card_number.isdigit():
        print("Invalid debit card number.")
        order_again()
    expiry_date = input("Enter expiry date (mm/yy): ")
    cvv = input("Enter CVV (3 digits): ") 
    if len(cvv) != 3 or not cvv.isdigit():
        print("Invalid CVV.")
        order_again()
    print("Thank you for your payment!") 
elif payment_choice == '4': 
    gcash_number = input("Enter GCash number (11 digits): ")
    if len(gcash_number) != 11 or not gcash_number.isdigit():
        print("Invalid GCash number.")
        print("Please enter your MPIN to confirm Payment")
        mpin = input("Enter MPIN : ")
        order_again()
    print("Thank you for your payment!") 
else: 
    print("Invalid choice. Your order has been cancelled.")
    order_again()


# Confirmation of order
print("Thank you for ordering! Here's your receipt:")
print("---------------------------------------------")   
# Calculate change
change = cash - total

# Display receipt
print("-------------- Receipt --------------")
print("Date:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("--------------------------------------")
print("Item\t\tQuantity\tPrice\t\tTotal")
print("--------------------------------------")
for item in order_summary:
    item_name, quantity, item_price, total_price = item
    print(f"{item_name}\t\t{quantity}\t\t{item_price}\t\t{total_price}")
print("--------------------------------------")
print(f"Subtotal:\t\t\t\t{total_price} pesos")
if discount_choice.lower() == 'y': 
    print(f"Discount ({discount_type}):\t\t\t-{total * discount[discount_type]} pesos")
if delivery_choice.lower() == 'd':
    print(f"Delivery charge:\t\t\t{delivery_charge} pesos")
print("--------------------------------------")
print(f"Total:\t\t\t\t\t{total} pesos")
print("-------------- Payment --------------")
print(f"Payment method: \t\t\t{'Cash' if payment_choice == '1' else 'Credit Card' if payment_choice == '2' else 'Debit Card' if payment_choice == '3' else 'GCash'}")
if payment_choice == '1':
    print(f"Amount tendered: \t\t\t{cash} pesos")
    print(f"Change: \t\t\t\t{change} pesos")
print("--------------------------------------")


