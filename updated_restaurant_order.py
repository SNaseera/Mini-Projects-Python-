#creating our menu
menu={
    'Pizza':120,
    'Burger':70,
    'Salad':60,
    'Pasta':60,
    'French Fries':70,
    'Coffee':70,
    'Sandwich':60
}

#Greeting the customer
print("Welcome to NAS Restaurant")
#Displaying menu
print("\tmenu\t")
print("Pizza\t\tRs 120\nBurger\t\tRs 70\nSalad\t\tRs 60\nPasta\t\tRs 60\nFrench Fries\tRs 70\nCoffee\t\tRs 70\nSandwich\tRs 60")
order_total = 0
item_1=input("Enter the name of dish you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is currently not available.")
for i in range(10):
    third_order = input("Do you want to add another item? (Yes/No)")
    if  third_order== "Yes":
        item_3 =input("Enter the name of dish = ")
        if item_3 in menu:
            order_total +=menu[item_3]
            print(f"Your item {item_3} has been added to your order")
    else:
        print(f"Ordered item {item_3} is currently not available.")
        break
print("Thanks for your order.")
print(f"The total amount of your items to pay is {order_total}")
