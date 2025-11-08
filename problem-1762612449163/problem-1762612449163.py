# Last updated: 8/11/2025, 8:04:09 pm
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)
        moves = 0
        for num in nums:
            moves += max_num - num

        return moves