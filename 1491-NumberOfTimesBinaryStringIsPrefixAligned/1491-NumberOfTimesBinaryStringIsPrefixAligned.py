# Last updated: 12/6/2025, 5:41:59 am
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        maxi = 0
        total = 0
        cnt = 0
        for i in light:
            if i > maxi:
                maxi = i
            total+=1
            if total == maxi:
                cnt += 1
        return cnt