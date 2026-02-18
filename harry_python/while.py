

# while(True):
#     n = input("enter a name: ")
#     if(len(n)<10):
#         print("sorry less char, at least 10 char include")
#     else:
#         print("user name are accepted")
#         break
    

row = int(input("Enter a row: "))
for i in range(row,0,-1):
    print("*" * i)