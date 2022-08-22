def check_palindrome(n):
    temp=n
    sum=0
    while temp>0:
        rem=temp%10
        sum=(sum*10)+rem
        temp=temp // 10
    if (sum==n):
        print("palindrpome")
    else:
        print("not a palindrome")

check_palindrome(int(input("enter a number:")))