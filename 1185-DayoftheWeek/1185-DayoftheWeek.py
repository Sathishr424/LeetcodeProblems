# Last updated: 3/8/2025, 6:08:16 pm
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        startDay = 5
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        days = startDay - 1
        for y in range(1971, year):
            if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
                days += 366
            else:
                days += 365
        
        for m in range(1, month):
            days += months[m - 1]
        
        days += day

        if month > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            days += 1
        
        return weekdays[days % 7]