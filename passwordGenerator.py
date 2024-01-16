import random




def easy_Password(n):
    random_letters1 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',k=n))
    print(random_letters1)


def medium_password(n):
    random_letters2 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789',k=n))
    print(random_letters2)

def hard_password(n):
     random_letters3 = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789-+*/!@#$%&',k=n))
     print(random_letters3)


choice = 0
while choice!=4:
    print("\nWelcome to Password generator")
    print("1.Easy level password")
    print("2.Medium level password")
    print("3.Difficult level password")
    print("4.EXIT")
    choice = int(input("Choose any one option:"))
    match choice:
        case 1:
            n = int(input("Enter the length of password:"))
            easy_Password(n)
        case 2:
            m = int(input("Enter the length of password:"))
            medium_password(m)
        case 3:
            l = int(input("Enter the length of password:"))
            hard_password(l)
        case 4:
            print("EXITING.....")
        case _:
            print("Invalid choice")

