a =int(input("enter a num1: "))
b =int(input("enter a num2: "))
c =int(input("enter a num3: "))

if(a>b and a>c):
    greater = a
elif(b>c):
    greater = b
else:
    greater = c


print("greatest number is ", greater)
