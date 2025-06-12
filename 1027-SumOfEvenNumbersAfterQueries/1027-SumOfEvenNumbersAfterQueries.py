# Last updated: 12/6/2025, 5:44:42 am
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = [False] * len(nums)
        tot = 0

        for i, num in enumerate(nums):
            if num % 2 == 0:
                evens[i] = True
                tot += num
        
        ret = []
        for x, i in queries:
            prev = nums[i]
            nums[i] += x
            if evens[i]:
                if nums[i] % 2 != 0:
                    tot -= prev
                    evens[i] = False
                else:
                    tot += x
            else:
                if nums[i] % 2 == 0:
                    tot += nums[i]
                    evens[i] = True
            ret.append(tot)
        
        return ret
