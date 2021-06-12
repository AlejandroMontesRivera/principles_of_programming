#       Option #2: Python Program to Check for Speed
#       Write a Python program to find the multiplication and division of two numbers.
#       Ask the user to input two numbers (num1 and num2). Given those two numbers,
#       multiply them together to find the output. Also, divide num1/num2 to find the output.
#       Compile and submit your source code and screenshots of the application executing the code and
#       the results in a single document.
#       Store input numbers

print(" Please insert two numbers to find the multiplication and division between them ")
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

#       Calculate multiplication and division
factor = float(num1) * float(num2)
division = float(num1) / float(num2)
# Display the multiplication
print('{0} multiply by {1} is {2}'.format(num1, num2, factor))
# Display the division
print('{0} divided  by {1} is {2}'.format(num1, num2, division))

