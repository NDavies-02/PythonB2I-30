while True:
    def findLetter():
        stringtoSearch=input("Please enter a string: ")
        charToFind=input("What character should we search for? ")
        result = charToFind in stringtoSearch
        if result==True:
            print("The character IS present in the string.")
        elif result==False:
            print("The character IS NOT present in the string.")
        
    def reverseString():
        stringtoReverse=input("Enter the string you'd like to reverse: ")
        print (stringtoReverse[::-1])

    choice=input("Please choose a function: A - String Search; or B - String Reversal: ")
    if choice in ["A", "a"]:
        findLetter()
        break
    elif choice in ["B", "b"]:
        reverseString()
        break
    else:
        print("Invalid selection.")
    
