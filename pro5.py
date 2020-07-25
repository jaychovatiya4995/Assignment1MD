#  prime number between 1 to 100

for i in range(1,101):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count += 1
    if count == 0 and i != 1 and i != 2:
        print(i,end=' ') 