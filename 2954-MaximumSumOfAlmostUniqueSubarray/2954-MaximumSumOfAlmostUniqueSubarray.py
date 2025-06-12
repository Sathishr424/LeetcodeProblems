# Last updated: 12/6/2025, 5:36:30 am
class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)

        hash = defaultdict(int)

        sum = 0
        for i in range(k):
            hash[nums[i]] += 1
            sum += nums[i]

        ret = sum if len(hash) >= m else 0

        for i in range(k, n):
            sum -= nums[i-k]
            j = i-k

            hash[nums[j]] -= 1
            if hash[nums[j]] == 0:
                del hash[nums[j]]
            
            hash[nums[i]] += 1
            sum += nums[i]
            if len(hash) >= m:
                ret = max(ret, sum)
        
        return ret


