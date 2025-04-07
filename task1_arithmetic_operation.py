try:
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    
    print('Addition:', num1 + num2)
    print('Subtraction:', num1 - num2)
    print('Multiplication:', num1 * num2)
    print('Division:', num1 / num2)
except ValueError:
    print('Error: Please enter valid integers.')
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
except Exception as ex:
    print('Unexpected Error:', ex)
