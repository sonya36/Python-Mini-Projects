menu = {
    'Pizza': 40,
    'Burger': 50,
    'Momo': 60
}
print("Welcome to Python Restaurant")
print('Pizza : 40\nBurger : 50\nMomo : 60\n')

order_total = 0
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print("Please order something else we can serve you.")

another_order = input("Do you want to order another item? (Yes/No): ")
if another_order == "Yes":
    item_2 = input("Enter the name of the item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print("Please order something else we can serve you.")
else:
    print("Thank you! Visit again.")

print(f"Your total order amount is: {order_total}")

