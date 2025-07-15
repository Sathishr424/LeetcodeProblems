# Last updated: 15/7/2025, 3:16:30 pm
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        op = 0
        def isSorted(nums):
            for i in range(len(nums)-1):
                if nums[i] > nums[i + 1]: return False
            return True
        
        while not isSorted(nums):
            n = len(nums)
            sortest = 0
            sortest_sum = nums[0] + nums[1]
            for i in range(n-1):
                s = nums[i] + nums[i + 1]
                if s < sortest_sum:
                    sortest_sum = s
                    sortest = i
            
            new_nums = []
            for i in range(n):
                if i == sortest:
                    new_nums.append(sortest_sum)
                elif i == sortest + 1: continue
                else:
                    new_nums.append(nums[i])
            nums = new_nums
            op += 1
        
        return op

