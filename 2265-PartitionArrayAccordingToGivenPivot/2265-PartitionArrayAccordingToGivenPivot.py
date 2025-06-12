# Last updated: 12/6/2025, 5:38:37 am
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [pivot] * len(nums)
        small = 0
        equal = 0
        for num in nums:
            if num < pivot:
                ans[small] = num
                small += 1
            elif num == pivot:
                equal += 1
        
        large = small+equal

        for num in nums:
            if num > pivot:
                ans[large] = num
                large += 1
        
        return ans

