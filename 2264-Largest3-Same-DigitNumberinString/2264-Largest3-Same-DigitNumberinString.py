# Last updated: 14/8/2025, 12:12:20 pm
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        good = ''

        for i in range(2, n):
            if num[i-2] == num[i-1] == num[i]:
                if good == '' or num[i] > good:
                    good = num[i]
        
        return good * 3