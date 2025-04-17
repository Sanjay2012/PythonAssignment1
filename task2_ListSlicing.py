# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements from the list
first_five = numbers[:5]

# Step 3: Reverse the extracted elements
reversed_list = first_five[::-1]

# Step 4: Print the extracted list and the reversed list
print("Original List", numbers)
print("Extracted first five elements:", first_five)
print("Reversed extracted elements:", reversed_list)
