# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is: {factorial(number)}")
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")
