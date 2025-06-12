# Last updated: 12/6/2025, 5:37:48 am
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ret = [0] * len(pref)
        ret[0] = pref[0]
        for i in range(1, len(pref)):
            ret[i] = pref[i] ^ pref[i - 1]
        return ret