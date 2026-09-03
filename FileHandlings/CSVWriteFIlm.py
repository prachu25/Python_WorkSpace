import csv

data = [

    ['Name', 'Relyear', 'Genre', 'Actor'],
    ['The Matrix', 1999, 'Action', 'keanu Reeves'],
    ['Sholay',1975,'Action','Amitabh Bachchan'],
    ['Dil se',1998,'Romance','Shah Rukh Khan']

]

with open("films.csv", "w", newline='') as file:
    write = csv.writer(file)
    write.writerows(data)


# benifit of with - is it automatically close the file we dont need to close manually