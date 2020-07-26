# check entered number is palindrome or not 

num = input('Enter Number to check it\'s palindrome or not : ' )
num2 = num[::-1]

if num == num2 :
    print(f'{num} is palindrome') 
else :
    print(f'{num} is not palindrome') 

