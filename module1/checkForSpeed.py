#       Option #2: Python Program to Check for Speed
#       Write a Python program to find the multiplication and division of two numbers.
#       Ask the user to input two numbers (num1 and num2). Given those two numbers,
#       multiply them together to find the output. Also, divide num1/num2 to find the output.
#       Compile and submit your source code and screenshots of the application executing the code and
#       the results in a single document.
#       Store input numbers

print(" Please insert two numbers to find the multiplication and division between them ")
while True:
    try:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))
    except ValueError:
        print("Only numbers are accepted inputs.")
#       Calculate multiplication and division
    else:
        factor = float(num1) * float(num2)
        division = 'undefined' if float(num2) == 0 else float(num1) / float(num2)
        #       Display the multiplication
        print('{0} multiply by {1} is {2}'.format(num1, num2, factor))
        # Display the division
        print('{0} divided  by {1} is {2}'.format(num1, num2, division))

