# Write a program to get data of 10 students in list and print them in ascending order of their
# name. The members of the list are as follows: 
# Name, City, Pincode, Course 
# 
# def stddata(name,city,pincode,course):  
#     return list(name,city,pincode,course)
# print(stddata("jay","surat",456474,"bca"))
stddata = []
for i in range(10):
    # print(i)
    i = input(('Enter student NAME,CITY,PINCODE,COURSE using sprated "," :')).split(",")
    stddata.append(i) 
print(f'Befor sortind Student Data : {stddata} ')

stddata.sort()
print(f' After Sorting Student Data : {stddata}') 

