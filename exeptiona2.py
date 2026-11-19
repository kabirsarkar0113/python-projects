try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    division = num1/num2
    print("This is the answer ",division)
except ZeroDivisionError:
    print("Number cannot be divided by zero")
except ValueError:
    print("Please enter valid whole numbers")
except:
    print("Wrong input")
else:
    print("No exception")
finally:
    print("Runs always")
