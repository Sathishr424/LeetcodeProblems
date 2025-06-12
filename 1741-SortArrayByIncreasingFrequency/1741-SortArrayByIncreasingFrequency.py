# Last updated: 12/6/2025, 5:40:42 am
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash = defaultdict(int)

        for num in nums: hash[num] += 1
        
        nums.sort(key=lambda x: [hash[x], -x])
        return nums