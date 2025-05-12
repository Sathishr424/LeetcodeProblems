# Last updated: 13/5/2025, 3:57:04 am
class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        exist = defaultdict(int)
        exist[0] += 1

        ret = 0
        cnt = 0
        for i, num in enumerate(nums):
            if num % modulo == k: 
                cnt += 1
                cnt %= modulo
            
            ret += exist[(cnt - k) % modulo]
            exist[cnt] += 1
        
        return ret