weight=float(input("Enter the weight in kg/lb:"))
unit=input("Enter the unit (kg/lb):").lower()
if unit=="kg":
    weight=weight*2.205
    unit="lbs"
    print(f"Your weight in pounds(lb) is {weight:.2f}{unit}.")
elif unit=="lb":
    weight=weight/2.205
    unit="kg" 
    print(f"Your weight in pounds(lb) is {weight:.2f}{unit}.")
