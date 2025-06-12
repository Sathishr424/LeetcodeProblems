# Last updated: 12/6/2025, 5:38:27 am
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash = defaultdict(int)

        for num in nums:
            hash[num] += 1

        for num in hash:
            if hash[num] % 2 != 0: return False
        
        return True