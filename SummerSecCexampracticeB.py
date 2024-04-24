#  LCCSSummer23-B 
# Name: 
# This function multiplies two numbers 
def multiply(x, y):
    return x * y 
# This function divides two numbers
def divide(x, y):
    return x / y
# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y

# Main Program
num_calculations = int(input("How many calculations will I do? "))
for i in range(1, num_calculations + 1):
    print(f"\nCalculation {i}:")

    print("Select operation.")
    print("1.Multiply")
    print("2.Divide")
    print("3.Add")
    print("4.Subtract")
    # Take input from the user 
    choice = input("Enter choice(1-4): ")

    num1 = int(input("Enter a first number: "))
    num2 = int(input("Enter a second number: "))

    if choice == '1':
        print(num1,"*",num2,"=", multiply(num1,num2))
    elif choice == '2':
        print(num1,"/",num2,"=", round(divide(num1,num2), 1))
    elif choice == '3':
        print(num1,"+",num2,"=", add(num1,num2))
    elif choice == '4':
        print(num1,"-",num2,"=", subtract(num1,num2))
    else:
        print("Invalid Number!")
