firstname = input("What is your name? ")
#user enters first name
surname = input("What is your surname? ")
print("Hello ", firstname , surname)
print("Please select from a list of items.\n")
print("\tItems Available")
print("------------------------")
print("1 Book")
print("2 Ruler")
print("3 Pen")
print("------------------------")
shoppingItem = int(input("\nEnter the number of items you would like: "))
if shoppingItem==1:
  print("you bought a book")
if shoppingItem==2:
  print("you bought a ruler")
if shoppingItem==3:
  print("you bought a pen")
if shoppingItem >3:
  print("Invalid choice. Goodbye!")