# Last updated: 12/6/2025, 5:44:48 am
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
            
            rem = s % k

            if prefix[rem]:
                ret += prefix[rem]
                if rem == (s-nums[i]) % k: ret -= 1
            
            prefix[rem] += 1
        
        return ret


