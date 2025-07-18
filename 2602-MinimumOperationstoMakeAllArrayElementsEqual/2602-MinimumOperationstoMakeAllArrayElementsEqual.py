# Last updated: 18/7/2025, 4:01:47 pm
class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        ret = []
        for num in queries:
            index = bisect_left(nums, num)
            
            left = (index * num) - prefix[index]
            right = (prefix[-1] - prefix[index]) - ((n - index) * num) 

            ret.append(left + right)
        
        return ret
