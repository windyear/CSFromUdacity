# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
def is_leap_year(year):
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return  False
    else:
        if year % 4 == 0:
            return True
        else:
            return False
    

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ##
    temp_month2 = month2
    days_Of_Months = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_Of_Months_of_leap =  [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #count the days from first year to the next year 
    if is_leap_year(year1):
        first_days = days_Of_Months_of_leap[month1 - 1] - day1
        while month1 < 13:
            first_days = first_days + days_Of_Months_of_leap[month1 -1]
            month1 = month1 + 1
    else:
        first_days = days_Of_Months[month1 - 1] - day1
        while month1 < 13:
            first_days = first_days + days_Of_Months[month1 -1]
            month1 = month1 + 1
     #count the days from the previous year of year2 to the  year2
    if is_leap_year(year2):
        last_days = days_Of_Months_of_leap[month2 - 1] - day2
        while month2 < 13:
            last_days = last_days + days_Of_Months_of_leap[month2 -1]
            month2 = month2 + 1
        last_days = 366 - last_days
    else:
        last_days = days_Of_Months[month2 - 1] - day2
        while month2 < 13:
            last_days = last_days + days_Of_Months[month2 -1]
            month2 = month2 + 1
        last_days = 365 - last_days
    # count the days between the year2 and year1
    year = year1+1
    days = 0
    while year < year2:
        if is_leap_year(year):
            days = days + 366
        else:
            days = days + 365
        year = year + 1
    days = days + first_days + last_days
    if year1 == year2 :
        if is_leap_year(year1):
            if temp_month2 <= 2:
                days = days - 368
            else:
                days = days - 366
        else:
            days = days - 365
    return days
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        print result
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
