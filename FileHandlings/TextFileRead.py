file = open("myinfo.txt","r")  # r-> read mode
contents = file.read()
print(contents)
file.close