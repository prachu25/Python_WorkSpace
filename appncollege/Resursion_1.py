#calculate sum of n natural number using Recursion

def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n

print(cal_sum(4))

# ----------------------------------------------------------

#calculate function to print all element in list

def printing(list,ind=0):
    if ind == len(list):
        return
    print(list[ind])
    printing(list,ind+1)

fruits = ["mango","apple","banana","chiku"]

printing(fruits)
#-----------------------------------------same using for in range
print()
for i in range(len(fruits)):
    print(fruits[i])

