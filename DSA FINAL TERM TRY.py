# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 17:09:42 2023

@author: BAD GAL RIRI
"""

# Coffee Shop Ordering System

# Item and Price list
menu = {'Espresso': 80, 'Americano': 100, 'Latte': 120, 'Mocha': 130, 'Cappuccino': 110}

# Discount list
discount = {'student': 0.2, 'senior': 0.3, 'pwd': 0.5}

# Delivery Charge
delivery_charge = 50

# Function for ordering

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
for item, price in menu.items():print(item + "\t\t" + str(price))
print("--------------------")

        
def order():
      print("Welcome to the coffee shop!")
      name = input("May I know your name please? ")
      print("Hello, " + name + "! Here's our menu:")
      print("--------------------")
for item, price in menu.items():
        print(item + "\t\t" + str(price))
        print("--------------------")
orders = {} 
    
    # User input for order selection 
while True:
        item = input("Please enter your order (enter 'stop' to finalize): ")
        if item == 'stop':
            break
        elif item in menu:
            quantity = int(input("How many? "))
            orders[item] = quantity
        else:
            print("Invalid item.")
    
    # Bubble sort for ordering
sorted_orders = sorted(orders.items(), key=lambda x: x[1])
print("Here's your order summary:")
print("--------------------")
total = 0
for item, quantity in sorted_orders:
        price = menu[item]
        subtotal = price * quantity
        print(item + "\t\t" + str(quantity) + "\t\t" + str(subtotal))
        total += subtotal 
        print("--------------------")
    
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
if payment_choice == '2': 
        card_number = input("Enter card number: ") 
        expiry_date = input("Enter expiry date (mm/yy): ")
        cvv = input("Enter CVV: ") 
        print("Thank you for your payment!") 
else: 
            print("Invalid choice.") 
            order()
# Confirmation of order
print("Thank you for ordering! Here's your receipt:")
print("---------------------------------------------")   
print("Customer name: ", name)
print("----------------------------------------------") 
print("Item : ", item) 
def order_again():               # Recursion method for ordering
    choice = input("Would you like to order again? (y/n) ") 
    if choice.lower() == 'y': 
        order() 
    elif choice.lower() == 'n': 
        print("Thank you for ordering!") 
    else: 
        print("Invalid choice.") 
        order_again()

