
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = num1 - num2
# Addition result of given Numbers
print("Sum of two Numbers : ",num1 + num2)

if num3 < 0:
   num3 = num3 *- 1

# Subtraction result of given Numbers
print("Difference between two Numbers : ",num3)

# Multiplication result of given Numbers
print("Product of two Numbers : ",num1 * num2)

# Division result of given Numbers
if num2 == 0:
   print("Division by zero can't be performed")
else:
    print("Division result of two Numbers : ",num1 / num2)
