# def show(n):
#     if n==0 :
#         return
#     print(n)
#     show(n-1)
# show(5)

# #fact using recursion
# def find_factorial(n):
#     if( n==1 or n==1):
#         return 1
#     return find_factorial(n-1)*n
#
# num = int(input("Enter the number: "))
# print(find_factorial(num))

# n =4
# sum =0
#
# for i in range(1,n+1):
#     sum+=i
# print("the sum is ", sum)

# def sum_of_naturalNumber(n):
#     sum=0
#     for i in range(1,n+1):
#         sum +=i
#     print("the sum is ", sum)
#
# sum_of_naturalNumber(5)

def cal_sum(n):
    if n == 0:
        return 0  
    return cal_sum(n-1) + n

sum =cal_sum(5)
print(sum)
