file = open("palyers.csv", "a")

nm = input('Enter name: ')
country = input('Enter Country: ')
sport = input('Enter Sport: ')


file.write(f"{nm},{country},{sport}\n")
file.close()