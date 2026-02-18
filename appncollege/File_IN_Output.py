# read demo file
# with open("demo.txt","r") as f:
#     data = f.read()
#     print(data)
#------------------------------

#write data , & directly creating a file if not exits already simply by writing file name
# with open("sample.txt","r+") as f:
#     data = f.read()
#     new_data = data.replace("java","python")
#     print(new_data)
#------------------------------------------------------
#deleting file
# random file create kele delete kra sathi
# with open("random.txt","w+") as f:
#     data = f.write("hey my name is prachi gorde\n and my semiar topic is socket programming in networking")
#     print(data)

#delete the above file-> random
# import os
# os.remove("random.txt")  # its delete file so iseliye dhikh nhi rahi hai
#-------------------------------------------------------------------


# que 1 - find learning word exits or not
word = "learning"
with open("sample.txt","r") as f:
    data = f.read()
    if(word in data):
        print("Found")
    else:
        print("Not Found")
#----------------------------------------------------------------