# weight converter
weight = float(input ("enter your weight: "))
unit = input("kilograms or pounds (K/L): " )
if unit == "K":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"your weight is: {round(weight, 1)} {unit}")
else:
    unit == "L"
    weight = weight / 2.205
    unit = "kgs."
    print(f"your weight is: {round(weight, 1)} {unit}")