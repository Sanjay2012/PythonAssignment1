# Task 2: Sum of Integers from 1 to 50 Using a Loop

def sum_1_to_50():
    total = 0
    for num in range(1, 51):
        total += num
    print(f"The sum of integers from 1 to 50 is: {total}")

if __name__ == "__main__":
    sum_1_to_50()
