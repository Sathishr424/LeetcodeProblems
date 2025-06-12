# Last updated: 12/6/2025, 5:38:10 am
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        ret = [0, 0]

        for num in counts:
            ret[1] += counts[num] % 2
            ret[0] += counts[num] // 2
        
        return ret