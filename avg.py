"""a = 10
b = 20
temp = a
a = b
b = temp
c = input("Enter the Value:")
print("value of a is ",a)
print("value of b is ",b)
print("Value of C is",c)
import os

def clear_terminal():
    if os.name == 'posix':  # for Unix/Linux/Mac
        _ = os.system('clear')
    elif os.name == 'nt':  # for Windows
        _ = os.system('cls')

# Call the function to clear the terminal
clear_terminal()
"""


def factorial(n):
    # Base case: If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
        
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)
        
        

# Example usage:
result = factorial(5)
print("Factorial of 5:", result)
