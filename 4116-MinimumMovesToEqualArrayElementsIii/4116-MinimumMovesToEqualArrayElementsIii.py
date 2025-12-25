# Last updated: 12/25/2025, 7:08:05 PM
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)

        max_num = max(nums)
        moves = 0
        for num in nums:
            moves += max_num - num

        return moves