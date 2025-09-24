# Last updated: 25/9/2025, 12:17:17 am
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)

        ret = []
        prev = 0

        for i in range(n):
            num = prev ^ pref[i]
            ret.append(num)
            prev ^= num

        return ret