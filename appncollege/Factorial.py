print("welcome to the factorial world of python")

num =int(input("Enter a number:"))
fact = 1

for i in range(1,num+1):
    fact*=i
print("the factorial of number is: ",fact)