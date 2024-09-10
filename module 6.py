#ex1
'''
import random
def roll_dice():
    return random.randint(1, 6)
roll_count = 0
while True:
        result = roll_dice()
        roll_count += 1
        print(f"Roll {roll_count}: {result}")
        if result == 6:
            print(f"You rolled a 6 after {roll_count} attempts!")
            break
'''
#ex2
'''
import random
def roll_dice(sides):
    return random.randint(1, sides)
sides = int(input("Enter the number of sides on the dice: "))
rolls = 0
result = 0
while result != sides:
    result = roll_dice(sides)
    rolls += 1
    print(f"Roll {rolls}: {result}")
print(f"It took {rolls} rolls to get {sides}.")
'''
#ex3
'''
def gallons_to_liters(gallons):
    return gallons * 3.78541
while True:
        gallons = float(input("Enter volume in gallons (negative to quit): "))
        if gallons < 0:
            print("Program ended.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons:.2f} gallons is equal to {liters:.2f} liters")
'''
#ex4
'''
def sum_list(numbers):
    return sum(numbers)
test_list = [1, 2, 3, 4, 5]
result=sum_list(test_list)
print(f'the sum of the numbers{test_list} is {result}')
'''
#ex5
'''
def filter_even_numbers(numbers):
    return[num for num in numbers if num%2 == 0]
original_list=[1,2,3,4,5,6,7,8,9,10]
filtered_list=filter_even_numbers(original_list)
print("original list:", original_list)
print("filtered list(even numbers only):", filtered_list)
'''
#ex6
'''
import math
def calculate_unit_price(diameter_cm, price_euros):
    radius_m = diameter_cm / 200
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price_euros / area_m2
    return unit_price
diameter1 = float(input("Enter the diameter of the first pizza (in cm): "))
price1 = float(input("Enter the price of the first pizza (in euros): "))
diameter2 = float(input("Enter the diameter of the second pizza (in cm): "))
price2 = float(input("Enter the price of the second pizza (in euros): "))
unit_price1 = calculate_unit_price(diameter1, price1)
unit_price2 = calculate_unit_price(diameter2, price2)
if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
else:
        print("Both pizzas have the same value for money.")
print(f"Unit price of first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of second pizza: {unit_price2:.2f} euros/m²")
'''