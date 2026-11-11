def greet():
    print("Welcome to the lemonade dispenser")

greet()

price_per_cup = float(input("Enter the price per cup"))
number_of_cups = int(input("Enter the number of cups"))

def calculate(x,y):
    total_cost = x*y
    return total_cost

Total_price = calculate(price_per_cup,number_of_cups)
print("Price_per_cup\n",price_per_cup,"Number_of_cups\n",number_of_cups,"Total price\n",Total_price)