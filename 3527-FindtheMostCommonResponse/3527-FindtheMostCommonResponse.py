# Last updated: 26/4/2025, 10:53:49 pm
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnts = defaultdict(int)

        ret = responses[0][0]
        for res in responses:
            uniq = {}
            for s in res:
                if s not in uniq:
                    cnts[s] += 1
                    uniq[s] = 1

        for s in cnts.keys():
            if cnts[s] > cnts[ret] or (cnts[s] == cnts[ret] and s < ret):
                ret = s

        return ret
            

            