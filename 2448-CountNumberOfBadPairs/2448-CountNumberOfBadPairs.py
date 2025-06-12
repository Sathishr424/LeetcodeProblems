# Last updated: 12/6/2025, 5:38:02 am
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        bad_pairs = 0
        diff_count = {}

        for pos in range(len(nums)):
            diff = pos - nums[pos]

            good_pairs_count = diff_count.get(diff, 0)

            bad_pairs += pos - good_pairs_count

            diff_count[diff] = good_pairs_count + 1

        return bad_pairs