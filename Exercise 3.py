string=input("Enter string to cipher: ")
string=list(string)
lettersnew=[]
for i in string:
    j=ord(i)+4
    k=chr(j)
    lettersnew.append(k)
    finalstring=''.join(lettersnew)
print("The 4-shift cipher is: " + finalstring)
input("Press any key to exit")
