# Write a program to get day, month and year from user and print the day falls on that date.
# i.e. if input is
# Input:
#  day : 25
#  month : 07
#  year: 2020
# Output : Saturday
# # (Hint: On Dt.01-01-1900, there was Monday)
import calendar

day = int(input('Enter day: '))
month = int(input("Enter month: ")) 
year = int(input('Enter year: '))
# dates = (day,month,year)  
# print(Date) 


dayNumber = calendar.weekday(year,month,day)
# calender = modual,weekday = function it's return indext number of days
# print(dayNumber) 
days = ['MONDAY','TUSEDAY','WENSDAY','THUSDAY','FRIDAY','SATURDAY','SUNDAY']
date = days[dayNumber]
#  days[indext] ex. days[6] then reutrn SUNDAY

# print(f'On Dt.{dates},There was {date}') 
print(f'On Dt.{day}-{month}-{year},There was {date}')

