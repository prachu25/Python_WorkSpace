#write a program to find the factorial of n
n = int(input("Enter a number: "))
# fact = 1
#
# for i in range(1,n+1):
#     fact*=i
#
# print(fact)

def find_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print("the factorial is ",fact)

find_fact(n)


