num = int(input("Enter a number: "))
rev = 0;

while num>0 :
    last_num = num%10
    rev = (rev*10) + last_num
    print(rev)
    num //=10

print()
print('the reverse is ', rev)

