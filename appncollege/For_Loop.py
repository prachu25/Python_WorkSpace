# tup = (1,3,4,6,45)
#
# for t in tup :
#     print(t)
#
# #printing list of names
# name = ("Rohit","virat","Dhoni","Jadu","Hardik","Ishan","Gill")
#
# for nm in name :
#     print(nm)
#
# # printing a string char
# nm = "Rohit"
# for ch in nm:
#     print(ch)

# PRINT THE LIST Using for loop
#
# list = [45,18,7,10,99,63,260]
#
# for item in list :
#     if item == 7:
#         continue
#     print(item)

# search a number in tuple using for loop
tup = (1,4,9,16,25,36,49,1)
n = int(input("Enter a number: "))
ind = 0
for i in tup:
    if n == tup[ind]:
        print("at index",ind)
        break
    ind+=1

else:
    print("not found")