# Last updated: 12/6/2025, 5:43:10 am
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        weeks = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        cnt = 365 * (year - 1971)
        for i in range(1972, year, 4):
            cnt += (i  % 4 == 0 and (i  % 100 != 0 or i  % 400 == 0))
        
        for i in range(month-1):
            cnt += months[i]
        if month > 2: cnt += year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        cnt += day

        return weeks[((cnt+4) % 7)]