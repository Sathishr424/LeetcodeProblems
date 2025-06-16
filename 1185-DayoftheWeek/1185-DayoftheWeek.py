# Last updated: 16/6/2025, 5:25:57 pm
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        start = 4 + (year - 1971) * 365
        month -= 1

        for y in range(1972, year, 4):
            start += y % 100 != 0 or y % 400 == 0
        
        for m in range(month):
            start += months[m]
        
        if month > 1 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            start += 1

        start += day
    
        return days[start % 7]