# Last updated: 5/7/2025, 8:45:38 am
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 501

        for num in arr:
            freq[num] += 1
        
        ret = -1
        for num in range(1, 501):
            if num == freq[num] and num > ret:
                ret = num
        
        return ret