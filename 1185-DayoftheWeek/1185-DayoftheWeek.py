# Last updated: 14/6/2025, 6:54:30 pm
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def decodeDate(date):
    return [int(d) for d in date.split('-')]

def getDays(year, month, date):
    days = (year - 1971) * 365 + date
    month -= 1

    for y in range(1972, year, 4):
        days += y % 100 != 0 or y % 400 == 0
    
    for m in range(month):
        days += months[m]
    
    if month > 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days += 1
    
    return days

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(getDays(*decodeDate(date1)) - getDays(*decodeDate(date2)))

        