# Last updated: 28/6/2025, 7:33:03 am
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        new_arr = []

        for i, num in enumerate(nums):
            new_arr.append((num, i))
        
        new_arr.sort(reverse=True)
        
        ret = sorted(new_arr[:k], key=lambda x: x[1])
        return [num for num, _ in ret]