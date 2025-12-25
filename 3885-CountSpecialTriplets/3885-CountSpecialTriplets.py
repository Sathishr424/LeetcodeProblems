# Last updated: 12/25/2025, 7:11:13 PM
class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        prev = defaultdict(int)
        after = defaultdict(int)

        for num in nums:
            prev[num] += 1
        
        after[nums[-1]] += 1
        prev[nums[-1]] -= 1
        
        n = len(nums)
        ret = 0
        for i in range(n-2, 0, -1):
            prev[nums[i]] -= 1

            curr = nums[i] * 2
            if prev[curr] and after[curr]:
                ret += prev[curr] * after[curr] % mod
                ret %= mod
            
            after[nums[i]] += 1

        return ret
            
                
        