# Last updated: 12/25/2025, 7:09:44 PM
class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        if k == 1: return 0
        n = len(nums)

        prefix = [0]
        s = 0
        for i in range(n):
            s = (s + nums[i]) % k
            prefix.append(s)

        relation = defaultdict(list)
        for i in range(len(prefix)):
            relation[prefix[i]].append(i)

        @cache
        def rec(index):
            if index >= n: return 0

            ans = rec(index + 1) + nums[index]
            i = bisect_right(relation[prefix[index]], index)

            if i < len(relation[prefix[index]]):
                ans = min(ans, rec(relation[prefix[index]][i]))

            return ans

        ans = rec(0)
        rec.cache_clear()
        return ans