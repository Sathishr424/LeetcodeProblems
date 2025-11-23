# Last updated: 23/11/2025, 6:05:40 am
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        if total % 3 == 0: return total

        need = total % 3
        max_ans = 0
        for num in nums:
            if num % 3 == need:
                max_ans = max(max_ans, total - num)
        
        nums.sort()
        need = (3 - total) % 3
        for num in nums:
            if num % 3 == need:
                total -= num
                if total % 3 == 0:
                    max_ans = max(max_ans, total)
                    break
        
        return max_ans