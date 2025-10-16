# Last updated: 16/10/2025, 4:24:45 pm
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        counter = [0 for _ in range(value)]

        for num in nums:
            counter[num % value] += 1
        
        current = 0
        while counter[current % value] > 0:
            counter[current % value] -= 1
            current += 1
    
        return current