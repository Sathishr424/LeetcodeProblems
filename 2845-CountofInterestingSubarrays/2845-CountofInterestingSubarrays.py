# Last updated: 25/4/2025, 10:41:13 pm
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        ret = 0
        cnt = 0

        for i, num in enumerate(nums):
            cnt += num % modulo == k

            ret += prefix[(cnt - k) % modulo]
            prefix[cnt % modulo] += 1
        
        return ret
        
            
