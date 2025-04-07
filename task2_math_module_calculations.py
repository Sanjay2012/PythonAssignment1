# Task 2: Using the Math Module for Calculations

import math
def calculate_math_functions():
    try:
        num = float(input("Enter a number: "))
        if num < 0:
            print("Natural logarithm and square root are not defined for negative numbers.")
            return
        
        square_root = math.sqrt(num)
        natural_log = math.log(num)
        sine_value = math.sin(num)  # input is in radians

        print(f"Square root of {num} = {square_root}")
        print(f"Natural logarithm of {num} = {natural_log}")
        print(f"Sine of {num} (in radians) = {sine_value}")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    calculate_math_functions()
