# Last updated: 12/6/2025, 5:43:14 am
class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }

        data = date.split(' ')
        date = data[0][:-2]
        month = months[data[1]]
        return f"{data[2]}-{'0' + str(month) if month <= 9 else month}-{'0' + date if len(date) == 1 else date}"