try:
    # Write user input to the file
    with open("output.txt", "w") as file:
        data = input("Enter text to write to the file: ")
        print(data)
        file.write("Hello, Python!\n")
        print("Data Successfully written to output.txt.")
        
    # Append additional data to the file
    with open("output.txt", "a") as file:
        additional_data = input("Enter additional text to append: ")
        print(additional_data)
        file.write("Learning File Handling in python.\n")
        print("Data is Successfully appended.")
        
    # Read and display the final content
    with open("output.txt", "r") as file:
        print("\nFinal content of 'output.txt':")
        content = file.read()
        print(content)
except Exception as e:
        print(f"An error occurred: {e}")