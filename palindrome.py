n=int(input('Enter the number '))
rev=0
temp=n
while(n>0):
    rem =n%10
    rev=rev*10+rem
    n=n//10
print('Reverse of the given number is ', rev)
if (temp==rev):
    print('The number is a Palindrome')
else:
    print('The number is not a palindrome')
