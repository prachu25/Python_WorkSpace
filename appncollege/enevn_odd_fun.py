def even_odd_checker(num):
    if num%2 == 0:
        print("Even Number ")
    else:
        print("Odd Number ")

n = int(input("enter a number: "))
even_odd_checker(n)


#print avg of 3 number
def avg_number(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)

avg_number(2,3,1)
