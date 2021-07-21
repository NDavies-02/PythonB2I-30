import math


def usrinput():
    a = int(input("Please enter the first number: "))
    b = int(input("Please enter the second number: "))
    return (a, b)


def selection(num1, num2):
    print("Please make a selection.")
    choice = input("1 - Calculate GCD; 2 - Calculate LCM; 3 - Help: ")
    if choice == "1":
        calcGCD(num1, num2)
    elif choice == "2":
        calcLCM(num1, num2)
    elif choice == "3":
        print("This simple program allows you to enter 2 numbers.")
        print("You can then choose to calculate the GCD or LCM of those numbers.")
        print("GCD = Greatest Common Denominator")
        print("LCM = Lowest Common Multiple")
        selection()


def calcGCD(a, b):
    result = math.gcd(a, b)
    result = str(result)
    print("The GCD is: " + result)


def calcLCM(a, b):
    result = math.lcm(a, b)
    result = str(result)
    print("The LCM is: " + result)


numbers = usrinput()
num1 = numbers[0]
num2 = numbers[1]
selection(num1, num2)
