menu = {"pizza": 100,
        "burger": 20,
        "coke": 10,
        "milkshake": 120,
        "fries": 50}
cart = []
Total = 0
price = 0

for key,value in menu.items():
    print(f"{key:<15}:{value}")

print("------------------------------")

while True:
    food = input("What you want(q to quit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("------------------------------")        
# print(*cart, end =" ")
 
for item in cart:
    qt = int(input(f"How many {item}s you want?"))
    if qt <= 0 :
        pass
    elif qt>0:
        print(f"{qt} {item} added.")
        print("------------------------------")
        price = menu[item]*qt
        Total += price
print("------------------------------")         
print(f"Your total is:{Total}")      
        

# for food in cart:
#     Total += menu.get(food)

# print()
# print("------------------------------") 
# print(f"Your total is: {Total}")             

