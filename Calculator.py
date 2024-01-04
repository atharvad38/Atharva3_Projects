import math

choice = 0

while choice != 6:
    print("\n")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Power")
    print("6.EXIT\n")

    choice = int(input("Choose any one option:\n"))

    if choice in [1, 2, 3, 4, 5]:
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))

    if choice == 1:
        print("Adding number 1 and number 2")
        print("Sum = ", num1+num2)
    elif choice == 2:
        print("Subtracting number 1 and number 2")
        print("Difference = ", num1-num2)
    elif choice == 3:
        print("Multiplying number 1 and number 2")
        print("Product = ", num1*num2)
    elif choice == 4:
        try:
             print("Dividing number 1 and number 2")
             print("division = ", num1/num2)
        except Exception as e:
             print(e)
    elif choice == 5:
        print("Number 1 raised to number 2:")
        print("Answer = ", math.pow(num1,num2))
    elif choice == 6:
        print("Exiting")
    else:
        print("INVALID CHOICE")



