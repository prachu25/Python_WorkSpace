num = int(input("enter a num: "))

if(num%7 == 0):
    print("multiple of 7")
else:
    print("NOT multiple of 7")



# IN ONE LINE
res = "multiple of 7" if num %7 == 0 else "NOT multiple of 7"

print(res)

