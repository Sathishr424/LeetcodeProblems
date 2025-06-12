# Last updated: 12/6/2025, 5:42:53 am
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        ret = 1
        hash = {}

        for a in arr:
            diff = a - difference
            if diff in hash:
                hash[a] = hash[diff] + 1
                ret = max(ret, hash[a])
            else:
                hash[a] = 1
        return ret
        