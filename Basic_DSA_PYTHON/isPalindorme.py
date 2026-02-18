# Palindrome Or Not
def is_palindrome(num):
    copy = num
    rev =0

    while num > 0:
        last_digit = num%10
        rev = (rev *10) +last_digit
        num//=10

    return True if copy == rev  else False

print(is_palindrome(1214))


# Armstrong Number Or Not
def is_armstrong_num(num):
    copy = num
    rev = 0
    sum =0

    while num > 0:
        last_digit = num%10
        sum = sum + (last_digit*last_digit*last_digit)
        num//=10

    return True if copy == sum else False

print(is_armstrong_num(3711))


