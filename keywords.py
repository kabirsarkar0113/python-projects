def change(paid,price):
    change == paid - price
    return change

snackprice = 22
print(f"Welcome to the vending machine. The price of the snack is {snackprice} and the acceptable coins - 1,5,10 and 25")

amount_inserted = 0
coins_inserted = 0

while True:
    coin = int(input("Insert coins"))
    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid")
        continue
    amount_inserted = coin + amount_inserted
    coins_inserted = coins_inserted + 1
    print("coins inserted",coins_inserted)
    print("Amount inserted",amount_inserted)
    if amount_inserted >= snackprice:
        print("Enough money inserted")
        break