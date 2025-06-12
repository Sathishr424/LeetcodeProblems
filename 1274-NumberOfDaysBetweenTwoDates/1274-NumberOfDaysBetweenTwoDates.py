# Last updated: 12/6/2025, 5:43:18 am
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        if date1 == date2: return 0
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def getDays(year, month, date):
            ret = date
            for i in range(month-1):
                ret += months[i]

            return ret + (month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

        date1 = date1.split('-')
        date2 = date2.split('-')

        if int(''.join(date2)) < int(''.join(date1)): 
            date1, date2 = date2, date1

        for i in range(3):
            date1[i] = int(date1[i])
            date2[i] = int(date2[i])

        days = 0
        for year in range(date1[0], date2[0]):
            days += 365 + (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
        return days - getDays(date1[0], date1[1], date1[2]) + getDays(date2[0], date2[1], date2[2])
        

        