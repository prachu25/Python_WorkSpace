
# Befinifit = with -> automatically close the file 

with open("myinfo.txt", "r") as file:
    contents = file.read()
    print(contents)