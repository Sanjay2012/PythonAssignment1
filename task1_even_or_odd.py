# Task 1: Check if a Number is Even or Odd

def check_even_odd():
    try:
        num = int(input("Enter an integer: "))
        if num % 2 == 0:
            print(f"{num} is an Even number.")
        else:
            print(f"{num} is an Odd number.")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    check_even_odd()
