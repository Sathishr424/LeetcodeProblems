# Last updated: 12/6/2025, 5:35:01 am
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == k: return max(nums)
        
        hash = defaultdict(int)

        for j in range(k):
            for i in range(j, n-j):
                hash[nums[i]] += 1

        ret = -1
        # [1, 2, 1]
        for num in nums:
            if hash[num] == 1:
                ret = max(ret, num)
        # print(dict(hash))
        return ret