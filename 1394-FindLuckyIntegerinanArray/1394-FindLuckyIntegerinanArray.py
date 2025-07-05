# Last updated: 5/7/2025, 8:44:46 am
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = defaultdict(int)

        for num in arr:
            freq[num] += 1
        
        ret = -1
        for num in freq:
            if num == freq[num]:
                ret = max(ret, num)
        
        return ret