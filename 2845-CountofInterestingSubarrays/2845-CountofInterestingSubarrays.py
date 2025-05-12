# Last updated: 13/5/2025, 3:52:24 am
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        exist = defaultdict(int)
        exist[0] += 1

        ret = 0
        cnt = 0
        for i, num in enumerate(nums):
            if num % modulo == k: 
                cnt += 1
                cnt %= modulo
            
            rem = cnt - k
            ret += exist[rem % modulo]

            exist[cnt] += 1
        
        return ret