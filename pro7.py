# check whether entered year is leap year or not.

year = int(input('Enter any year :'))

if year%4 == 0 :
    print(f'{year} is leap year')
else :
    print(f'{year} is not leap year')
    