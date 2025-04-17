# Step 1: Create a dictionary of student names and their marks
student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90,
    "Eve": 88
}

# Step 2: Ask the user to input a student's name
student_name = input("Enter the student's name: ")

# Step 3 & 4: Retrieve and display the corresponding marks or an appropriate message
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Student '{student_name}' not found.")
