# Last updated: 16/7/2025, 6:42:30 pm
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        ret = 0

        diffs = defaultdict(int)
        for i in range(n):
            for j in range(i+1, n):
                diffs[nums[j] - nums[i]] = 1

        # 4, 6 => 2
        # 6, 4 => -2
        for diff in diffs:
            counter = [0] * (maxi * 3 + 1)
            for i in range(n):
                counter[nums[i] + maxi] = counter[ (nums[i] - diff + maxi) ] + 1
                ret = max(ret, counter[nums[i] + maxi])
            # print(diff, [(i, counter[i]) for i in range(maxi + 1) if counter[i] > 0])
        return ret

