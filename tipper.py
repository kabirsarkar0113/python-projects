def calculate(x,y):
    total = x*(1+0.01*y)
    total = round(total,2)
    print(f"Your total amount is {total}")

bill_amount = float(input("Your bill amount "))
tip_perc = float(input("tip %"))

calculate(bill_amount,tip_perc)