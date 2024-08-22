#ex1
'''
number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1
'''
#ex2
'''
def inch_to_cm(inches):
    return inches * 2.54


print("Inch to Centimeter Converter")
print("Enter a negative value to exit.")

while True:
    inches = float(input("Enter length in inches: "))

    if inches < 0:
        print("Negative value entered. Exiting the program.")
        break

    centimeters = inch_to_cm(inches)
    print(f"{inches} inches is equal to {centimeters:.2f} centimeters.")

print("Thank you for using the converter!")
'''
#ex3
'''
def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers


def main():
    print("Enter numbers one at a time. Press Enter without typing a number to finish.")
    numbers = get_numbers()

    if not numbers:
        print("No numbers were entered.")
    else:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"The smallest number is: {smallest}")
        print(f"The largest number is: {largest}")


if __name__ == "__main__":
    main()
'''
#ex4
'''
import random


def number_guessing_game():
    # Generate a random number between 1 and 10
    secret_number = random.randint(1, 10)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10.")

    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 10.")
            continue

        # Check if the guess is valid
        if guess < 1 or guess > 10:
            print("Please enter a number between 1 and 10.")
            continue

        # Compare the guess with the secret number
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Correct! You've guessed the number!")
            break

    print("Thanks for playing!")


# Run the game
number_guessing_game()
'''
#ex5
'''
def check_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and \
           any(c.islower() for c in password) and any(c.isdigit() for c in password)

def login():
    correct_username = "python"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        username = input("Nhập tên người dùng: ")
        password = input("Nhập mật khẩu: ")

        if username == correct_username and check_password(password):
            print("Welcome")
            return True
        else:
            attempts += 1
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"Tên người dùng hoặc mật khẩu không đúng. Còn {remaining_attempts} lần thử.")
            else:
                print("Access denied")
                return False

login()
'''
#ex6
'''
import random
import math


def approximate_pi(num_points):
    points_inside_circle = 0

    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        # Check if the point is inside the unit circle
        if x ** 2 + y ** 2 < 1:
            points_inside_circle += 1

    # Calculate the approximation of pi
    pi_approximation = 4 * points_inside_circle / num_points
    return pi_approximation


def main():
    print("Pi Approximation using Monte Carlo Method")
    print("=========================================")

    while True:
        try:
            num_points = int(input("Enter the number of random points to generate: "))
            if num_points <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer.")

    approximated_pi = approximate_pi(num_points)

    print(f"\nApproximation of pi: {approximated_pi}")
    print(f"Actual value of pi: {math.pi}")
    print(f"Difference: {abs(math.pi - approximated_pi)}")


if __name__ == "__main__":
    main()
'''