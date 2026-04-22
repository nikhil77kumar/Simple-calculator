#Printing simple calculator
print("Simple Calculator")

def for_sum(num1, num2):
    return num1+num2

def for_diff(num1, num2):
    return num1-num2

def for_product(num1, num2):
    return num1*num2

def for_division(num1, num2):
    return num1/num2

print("1 for Addition")
print("2 for Subtraction")
print("3 for Multiplication")
print("4 for Division")

Number1 = int(input("Enter num1: "))
Number2 = int(input("Enter num2: "))

choice = input("Enter choice: ")

if (choice == "1"):
    print("The Answer is:",for_sum(Number1 ,Number2))

if (choice == "2"):
    print("The Answer is:",for_diff(Number1 ,Number2))

if (choice == "3"):
    print("The Answer is:",for_product(Number1 ,Number2))

if (choice == "4"):
    print("The Answer is:",for_division(Number1 ,Number2))