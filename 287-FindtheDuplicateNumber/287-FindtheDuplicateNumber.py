# Last updated: 1/6/2025, 9:01:39 pm
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = int(log2(n-1)) + 1
        
        cnt = [0] * l
        for num in nums:
            index = l-1
            while num:
                cnt[index] += num % 2
                num //= 2
                index -= 1

        for num in range(1, n):
            index = l-1
            while num:
                cnt[index] -= num % 2
                num //= 2
                index -= 1

        ret = 0
        index = 0
        while cnt:
            if cnt.pop() > 0:
                ret += 2 ** index
            index += 1
        
        return ret