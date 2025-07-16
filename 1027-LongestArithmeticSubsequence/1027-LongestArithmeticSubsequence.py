# Last updated: 16/7/2025, 6:34:01 pm
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = max(nums)
        ret = 0
        # 4, 6 => 2
        # 6, 4 => -2
        for diff in range(-maxi, maxi + 1):
            counter = defaultdict(int)
            for i in range(n):
                need = nums[i] - diff

                counter[nums[i]] = max(1, counter[need] + 1)
                ret = max(ret, counter[nums[i]])
            # print(diff, [(i, counter[i]) for i in range(maxi + 1) if counter[i] > 0])
        return ret

