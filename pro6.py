# Check Number is prime or not prime

n = int(input("Enter number to check is prime or not :"))
i=2
j=0
while i < n:
    if n%i == 0:
        j += 1 
        break
    i += 1
if j == 0 and n != 1:
    print(f'{n} is Prime Number')
else:
    print(f'{n} is Not Prime Number')
    