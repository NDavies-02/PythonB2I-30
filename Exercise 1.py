import math


def usrinput():
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    return (a, b)


def selection(num1, num2):
    print("")
    print("Please make a selection.")
    choice = input("1 - Calculate GCD; 2 - Calculate LCM; 3 - Pick New Numbers;  4 - Help: ")
    print("")
    if choice == "1":
        calcGCD(num1, num2)
    elif choice == "2":
        calcLCM(num1, num2)
    elif choice == "3":
        newnumbers = usrinput()
        new1 = newnumbers[0]
        new2 = newnumbers[1]
        selection(new1, new2)
    elif choice == "4":
        print("This simple program allows you to enter 2 numbers.")
        print("You can then choose to calculate the GCD or LCM of those numbers.")
        print("GCD = Greatest Common Denominator")
        print("LCM = Lowest Common Multiple")
        selection(num1, num2)
    else:
        print("Invalid selection.")
        selection(num1,num2)


def calcGCD(a, b):
    result = math.gcd(a, b)
    result = str(result)
    print("")
    print("The GCD of " + str(a) + " and " + str(b) +" is: " + result)


def calcLCM(a, b):
    result = math.lcm(a, b)
    result = str(result)
    print("")
    print("The LCM of " + str(a) + " and " + str(b) +" is: " + result)

numbers = usrinput()
num1 = numbers[0]
num2 = numbers[1]
selection(num1, num2)
