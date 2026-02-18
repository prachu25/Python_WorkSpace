#
# print("multiplication table world")
# num =int(input("Enter a number: "))
#
# i = 1
# while i<=10 :
#     print(f"{num} x {i} = {num*i}")
#     i+=1

# nums = [1,4,9,16,25]
#
# # print(nums[1])
#
# i =0
# while i<=len(nums)-1 :
#     print(nums[i])
#     i+=1

# print the movies names using loop
# movie1 = input("Enter a movies tile: ")
# movie2 = input("Enter a movies tile: ")
# movie3 = input("Enter a movies tile: ")
#
# movies = []
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
#
# print(movies)
# i = 0
# while i < len(movies) :
#     print(movies[i])
#     i+=1
#
# print("end ")

# Tuple of numbers
numbers = (24, 15, 23, 56, 99, 98, 100, 99)

while True:
    try:
        target = int(input("Enter your target: "))
    except Exception:
        print("Invalid input! Please enter a number.")
        continue  # ask again if input is invalid

    i = 0
    found = False
    while i < len(numbers):
        if numbers[i] == target:
            print(f"Found at index {i} and the element is {numbers[i]}")
            found = True
        i += 1

    if found:
        break  # stop the loop if target is found
    else:
        print("Try again, target is not found.")
