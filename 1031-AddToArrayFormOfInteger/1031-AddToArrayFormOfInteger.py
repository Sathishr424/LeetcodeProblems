# Last updated: 12/6/2025, 5:44:41 am
# 274
# 181

class Solution:
    def addToArrayForm(self, nums: List[int], k: int) -> List[int]:
        ret = deque([])

        for i in range(len(nums)-1, -1, -1):
            val = nums[i] + (k % 10)
            k = (k // 10) + (val // 10)
            ret.appendleft(val % 10)

        while k:
            ret.appendleft(k % 10)
            k //= 10
        
        return ret

