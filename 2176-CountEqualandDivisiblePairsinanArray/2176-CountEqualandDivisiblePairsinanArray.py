# Last updated: 17/4/2025, 8:17:07 am
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        hash = defaultdict(list)
        ret = 0
        for i, num in enumerate(nums):
            for j in hash[num]:
                if i * j % k == 0: ret += 1
            
            hash[num].append(i)
        
        return ret