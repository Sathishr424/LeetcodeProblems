# Last updated: 12/6/2025, 5:43:22 am
class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = 0
        month = int(date[5:7])-1
        year = int(date[:4])
        date = int(date[8:])

        for i in range(month):
            days += months[i]
        
        if month >= 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days += 1
        return days+date
