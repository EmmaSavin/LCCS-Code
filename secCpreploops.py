#fname = input("enter a first name ")
#sname = input("enter a second name ")

while True:
    fname = input("enter a first name ")
    sname = input("enter a second name ")
    print("running while loop")
    check=input("do you want the loop to continue? Y/N ")
    if check in ("Y","y"):
        print("continuing loop")
    else:
        break