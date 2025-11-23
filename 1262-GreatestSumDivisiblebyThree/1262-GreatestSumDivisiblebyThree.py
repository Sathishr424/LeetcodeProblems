# Last updated: 24/11/2025, 1:45:17 am
cmax = lambda x, y: x if x > y else y

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        if total % 3 == 0: return total

        nums.sort()
        need = total % 3
        max_ans = 0
        for num in nums:
            if num % 3 == need:
                max_ans = cmax(max_ans, total - num)
                break
        
        need = (3 - total) % 3
        for num in nums:
            if num % 3 == need:
                total -= num
                if total % 3 == 0:
                    max_ans = cmax(max_ans, total)
                    break
        
        return max_ans