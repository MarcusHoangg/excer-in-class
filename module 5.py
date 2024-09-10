#ex1
'''
print("this program will calculate the sum of all dice rolls")
import random as rand
totalDice=int(input("Enter the total number of dice rolls: "))
dice=0
SumOfDice=0
for i in range(totalDice):
    dice= rand.randint(1, 6)
    SumOfDice+=dice
print("the sum of all dice results is {sum}".format(sum=SumOfDice))
'''
#ex2
'''
print("this program will print out 5 greatest number form the set of inputted numbers in descending order")
numList=[]
while True:
    num=int(input("Enter the number ( or an empty string to stop program ): "))
    try:
        numList.append((float(num)))
    except:
        if num == '': break
        else : print("invalid input")

numList.sort(reverse=True)
if len(numList)<5:
    print("there is less than 5 numbers is the list")
    exit()
print("the five greatest numbers in descending order are : ",end='')
for i in range(5):
    print(numList[i],end=' ')
'''
#ex3
'''
print("this program will check whether your input number is prime")
num=int(input("Enter the number : "))
i=2
checker = False
if num ==1 : print('your number is not a prime')
elif num ==2 : print('your number is not a prime')
else:
    while(i*i<=num):
      if(num%i==0):
          print('your number is not a prime')
          checker = True
          break
      else :
          i=i+1
    if checker ==0 : print('your number is not a prime')
'''
#ex4
'''
print("this program will ask you to enter 5 cities name and output them one by one ")
CityList=[]
for i in range(1,6):
    city = input(f'enter city {i} name:')
    CityList.append(city)
for i in CityList:
    print(i)
'''