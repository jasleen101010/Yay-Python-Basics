# Number of Days per Month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Check for Leap Year
def isLeapYear(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


# Check for Days in a Month
def daysInAMonth(year, month):

    if month not in range(1, 13):
        return "Invalid Month"

    if month == 2 and isLeapYear(year):
        return 29

    return month_days[month]


# Main Method
if __name__ == '__main__':
    print(daysInAMonth(2016, 16))
