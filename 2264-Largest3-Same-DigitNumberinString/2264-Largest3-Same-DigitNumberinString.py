# Last updated: 14/8/2025, 11:57:03 am
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = len(num)
        ret = ''

        for i in range(2, n):
            if num[i-2] == num[i-1] == num[i]:
                good = num[i-2] + num[i-1] + num[i]
                if ret == '' or good > ret:
                    ret = good
        
        return ret