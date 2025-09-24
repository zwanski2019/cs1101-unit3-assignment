# Assignment Unit 3 - Question 2
# Author: Mohamed Ibrahim

# Deliberate runtime error example
print("=== Runtime Error Example ===")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    print("Result:", a / b)
except ZeroDivisionError as e:
    print("Runtime Error:", e)

# Corrected version with handling
print("\n=== Safe Division Example ===")
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

if b == 0:
    print("Error: Division by zero is not allowed.")
else:
    print("Result:", a / b)
