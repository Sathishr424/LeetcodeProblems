# Last updated: 25/4/2025, 3:43:10 pm
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ret = 0
        n = len(nums)
        s = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for i in range(n):
            
            s += nums[i]

            if nums[i] % k == 0: ret += 1

            if prefix[s % k]:
                ret += prefix[s % k]
                if s % k == (s-nums[i]) % k: ret -= 1
            
            prefix[s % k] += 1
        
        return ret


