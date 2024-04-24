#  LCCSSummer23-A 
# Name:
name = str(input("Please enter your name: "))
print("Hello", name)
print("Welcome to the addition and subtraction calculator")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#This calculator can only add and subtract

while True:
    print('Do you want me to (a)dd or (s)ubtract?')
    choice = input()

    resultadd = (num1 + num2)
    resultsubtract = (num1 - num2)

    if choice == 'a' or choice == 'A':
        print(num1, "+", num2, "=", resultadd)
        break
    elif choice == 's' or choice == 'S':
        print(num1, "-", num2, "=", resultsubtract)
        break
    else:
        print("Invalid Option!")
