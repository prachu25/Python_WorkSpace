word = input("Enter a Word: ")

is_palindrome = True

start = 0
end = len(word) -1

while(start < end):
    if(word[start] != word[end]):
        is_palindrome = False
        break
    start+=1
    end-=1

if(is_palindrome):
    print("is  palindrome")
else:
    print("Not palindrome")


#COUNT GRADE
grade = ["C", "A" ,"B","A","B","C","A"]
print(grade.count("C"))
grade.sort()

print(grade)