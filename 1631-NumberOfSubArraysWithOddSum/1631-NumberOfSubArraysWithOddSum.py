# Last updated: 12/6/2025, 5:41:11 am
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        pref = 0
        ret = 0
        odd = 0
        even = 1
        for num in arr:
            pref += num
            if pref % 2 == 0: 
                even += 1
                ret += odd
            else:
                odd += 1
                ret += even
            
            ret %= MOD

        return ret