
"""Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""

num1 = int(input("Enter first number  "))
num2 = int(input("Enter second number  "))

print(num1)
print(num2)

print('Maximum number between',num1, 'and', num2, 'is',  max(num1,num2))

print("power", num1, 'to', num2, 'is', pow(num1,num2))

print("addition of", num1, 'and',num2, 'is', num1+num2)
print("substraction of", num1, 'and',num2, 'is', num1-num2)

print("Multiplication of", num1, 'and',num2, 'is', num1*num2)
print("Division of", num1, 'and',num2, 'is', num1/num2)


print("Formated_num1 is : ", f"{num1 : .5f}")
print("Formated_num2 is : ", f"{num2 : .5f}")