# print serice 1,2,4,7,11,16,22 ....

n = int(input('Enter value for n : '))

j = 1

for fib in range(0,n-1):
    fib = fib + j 
    j = fib 
    print(fib) 

