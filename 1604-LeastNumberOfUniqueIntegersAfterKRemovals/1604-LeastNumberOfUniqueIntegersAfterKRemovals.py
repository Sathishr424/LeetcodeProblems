# Last updated: 12/6/2025, 5:41:20 am
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hash = defaultdict(int)

        for num in arr:
            hash[num] += 1
        
        nums = []

        for num in hash:
            nums.append((num, hash[num]))
        
        nums.sort(key=lambda x: x[1])

        for i, (num, freq) in enumerate(nums):
            k -= freq
            if k == 0: return len(nums) - i - 1
            elif k < 0: return len(nums) - i
        
        return 0
