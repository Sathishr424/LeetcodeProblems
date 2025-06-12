# Last updated: 12/6/2025, 5:42:34 am
class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        hash = defaultdict(list)
        ret = []
        for i,size in enumerate(gs):
            hash[size].append(i)
            if len(hash[size]) == size:
                ret.append(hash[size])
                hash[size] = []

        return ret

        