# check entered text is palindrome or not 
str1 = input("Enter text to check it's palindrome or not :")
str2 = str1.upper() 
str3 = str2[::-1]   
# print(str2)  

if str2 == str3 :
    print(f'{str1} is palindrome') 
else :
    print(f'{str1} is not palindrome') 