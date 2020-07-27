# write program to get 10 values in the list and sort them using bubble sort method

list1 = input(('Enter 9 values using spreated "," : ')).split(",") 
print(list1) 

for i in range(len(list1)-1,0,-1):
    for j in range(i):
        if list1[j] > list1[j+1]:
            temp=list1[j]
            list1[j]=list1[j+1]
            list1[j+1]=temp 
print(list1) 

# for i in range(0,11):
#     for j in range(i+1,11):
#         if list1[i] >= list1[j]:
#             temp = list1[i]
#             list1[i] = list1[j]
#             list1[j] = temp
# print(list1)