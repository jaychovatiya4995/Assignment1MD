#  print series 1,3,5,9....n (odd number)

n = int(input('Enter any value for n :'))

for i in range(1, n + 1):  
    if(i%2 != 0):
        print(i,end=',')  
    

