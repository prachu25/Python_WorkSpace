file = open("myskills.txt", "a")
lines = input('Enter a line to store in files: ')
file.write(f"{lines}\n")
file.close()