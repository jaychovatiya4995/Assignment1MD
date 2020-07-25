# fibbonacci series
n = int(input('Enter value for n to serach fibbonacci :'))
a = 0
b = 1
print(a,b,end=' ') 
for i in range(2,n+1):
    i = a + b
    if i <= n:
        print(i,end=" ") 
    a = b
    b = i 
    
         
    
