#Case Study:
#You have been hired to develop a program that will calculate the total price of a customer's 
#shopping cart. The program will prompt the user to enter the price of each item and the quantity 
#they wish to purchase. Once all the items have been entered, the program will calculate the total 
#price, including any applicable discounts or delivery fees.
#The program should meet the following specifications:
#1. The program will prompt the user to enter the price of each item and the quantity they wish to 
#purchase.
#2. The program will allow the user to enter up to 10 items.
#3. If the total price is over $100, the program will apply a 10% discount to the total price.
#4. If the total price is less than $50, the program will add a $5 delivery fee to the total price.
#5. The program will display the total price, including any discounts or delivery fees.


def calculate_total_price():
    total_price = 0
    num_items = int(input("Enter the number of items (up to 10): "))

    # Validate the number of items
    if num_items > 10:
        print("Error: Number of items cannot exceed 10.")
        return

    for i in range(num_items):
        price = float(input(f"Enter the price of item {i + 1}: $"))
        quantity = int(input(f"Enter the quantity of item {i + 1}: "))
        total_price += price * quantity

    # Calculate discount and total amount after discount
    discount = 0
    if total_price > 100:
        discount = total_price * 0.1
    total_amount_after_discount = total_price - discount

    # Add delivery fee if applicable
    if total_price < 50:
        delivery_fee = 5
        total_amount_after_discount += delivery_fee
    else:
        delivery_fee = 0

    print(f"Total amount: ${total_price:.2f}")
    print(f"Discount: ${discount:.2f}")
    print(f"Delivery fee: ${delivery_fee:.2f}")
    print(f"Amount to be paid after discount and delivery fee: ${total_amount_after_discount:.2f}")


calculate_total_price()
