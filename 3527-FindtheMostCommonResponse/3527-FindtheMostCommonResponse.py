# Last updated: 26/4/2025, 10:29:09 pm
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnts = defaultdict(int)

        for i, res in enumerate(responses):
            uniq = {}
            for s in res:
                if s not in uniq:
                    cnts[s] += 1
                    uniq[s] = 1

        arr = sorted(cnts.keys())
        ret = arr[0]
        for s in arr:
            if cnts[s] > cnts[ret]:
                ret = s

        return ret
            

            