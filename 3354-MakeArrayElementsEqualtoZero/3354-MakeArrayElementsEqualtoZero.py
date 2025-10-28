# Last updated: 28/10/2025, 2:11:53 pm
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]

        for num in nums:
            prefix.append(prefix[-1] + num)
        # print(prefix)
        cnt = 0
        for i in range(n):
            if nums[i] == 0:
                right = prefix[-1] - prefix[i]
                left = prefix[i]
                # print(i, left, right)
                if left == right: cnt += 2
                elif abs(left - right) == 1: cnt += 1
        
        return cnt