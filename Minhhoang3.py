'''
a = int(input("A is "))
b = int(input("B is "))
print(a)
print(b)
c = a
a = b
b=c
print(a)
print(b)
'''
import math
import random

#ex1
'''
name = input("Enter your name: ")
print ("Nice to meet you ", name)
'''
#ex2
'''
rds = float(input("Enter your rds: "))
area = math.pi*(rds)**2
print("The area of your circle is ", area)
'''
#ex3
'''
length = float(input("Enter your length: "))
width = float(input("Enter your width: "))
perimeter = (length*width)*2
print("Your perimeter is ", perimeter)
'''
#ex4
'''
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
num3 = float(input("Enter your third number: "))
sum=int(num1+num2+num3)
average=int(sum/3)
print("Your average is ", average)
'''
#ex5
'''
talent=float(input(f"Enter your talent: \n"))
pounds=float(input(f"Enter your pounds: \n")) + (talent *20)
lots= float(input(f"Enter yourlots: \n")) + (pounds *32)
grams = lots*13.3
kilograms= int((grams-(grams % 1000)) / 1000)
grams_left = grams - (kilograms*1000)
print("the weight in modern units:", grams_left)
'''
#ex6
'''
import random
code1=random.randint(0,9)
code2=random.randint(0,9)
code3=random.randint(0,9)
print(f"{code1} and {code2} and {code3}")
'''
''''
code1=random.randint(1,6)
code2=random.randint(1,6)
code3=random.randint(1,6)
print(f"{code1} and {code2} and {code3}")
'''




