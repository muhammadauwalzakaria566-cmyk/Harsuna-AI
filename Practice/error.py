try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")
    