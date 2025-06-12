# Last updated: 12/6/2025, 5:38:35 am
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indexes = defaultdict(list)
        ret = 0

        for i, num in enumerate(nums):
            for j in indexes[num]:
                if i * j % k == 0: ret += 1
            
            indexes[num].append(i)
        
        return ret