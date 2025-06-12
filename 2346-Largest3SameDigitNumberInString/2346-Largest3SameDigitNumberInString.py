# Last updated: 12/6/2025, 5:38:22 am
class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        ans = -1
        prev = None
        cnt = 0
        
        for num in nums:
            if num == prev:
                cnt += 1
            else:
                if cnt >= 3 and int(prev) > ans:
                    ans = int(prev)
                prev = num
                cnt = 1
        if cnt >= 3 and int(prev) > ans:
            ans = int(prev)
        return str(ans) * 3 if ans != -1 else ""