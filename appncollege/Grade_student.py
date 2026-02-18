mark = int(input("enter mark: "))

if(mark >= 90) :
    grade = "A"
elif(mark >= 80 and mark < 90) :
    grade = "B"
elif(mark >=70 and mark < 80):
    grade = "C"
else :
    grade = "D"

print("grade of the student is -> ",  grade)
