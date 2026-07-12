region = ("jos","plateau",  "dogon karfe")
print(region)
hausa_laters = {"A", "B", "b", "d", "k", "y", "A"} 
print(hausa_laters)

try:
    number = int(input("Enter a number: "))
    print(100 / number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("That's not a valid number!")