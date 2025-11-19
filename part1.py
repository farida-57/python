
print("=== WELCOME TO SUNRISE COFFEE ===")
print("We have a discount of 200 CFA when you take at least 2 of each menu item.")
print("Please enter the order details of the customer.\n")

# Customer order information
customer_name = input("Enter the name of the customer: ")
customer_age = int(input("Enter the age of the customer: "))
membership_status = input("Are you a Sunrise Coffee member? (yes/no): ")
order_type = input("Is this order for take-away ? (yes/no): ")


coffee_quantity = int(input("Enter the number of coffees taken: "))
tea_quantity = int(input("Enter the number of teas taken: "))
sandwich_quantity = int(input("Enter the number of sandwiches taken: "))

# Unit price of each menu item
coffee_price = float(input("What is the unit price of coffee: "))
tea_price = float(input("What is the unit price of tea: "))
sandwich_price = float(input("What is the unit price of sandwich: "))
discount = float(input("Enter discount amount (0 if none): "))

# Calculations
total_coffee = coffee_quantity * coffee_price
total_tea = tea_quantity * tea_price
total_sandwich = sandwich_quantity * sandwich_price
subtotal = total_coffee + total_tea + total_sandwich
total_due = subtotal - discount

# Summary
print("\n=== Order Summary ===")
print(f"Customer: {customer_name} ({customer_age} years old)")
print(f"Membership status: {membership_status}")
print(f"Coffee total: {total_coffee} CFA")
print(f"Tea total: {total_tea} CFA")
print(f"Sandwich total: {total_sandwich} CFA")
print(f"Subtotal: {subtotal} CFA")
print(f"Discount: {discount} CFA")
print(f"Total amount due: {total_due} CFA")
print(f"Order type: {order_type}")
print("\nThank you for your order at Sunrise Coffee!")