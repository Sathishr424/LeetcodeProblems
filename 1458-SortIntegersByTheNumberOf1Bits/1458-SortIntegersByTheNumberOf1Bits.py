# Last updated: 12/6/2025, 5:42:14 am
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        hash = defaultdict(list)
        for a in arr:
            hash[bin(a).count('1')].append(a)
        ret = []
        for k in sorted(list(hash.keys())):
            for a in sorted(hash[k]):
                ret.append(a)
        return ret