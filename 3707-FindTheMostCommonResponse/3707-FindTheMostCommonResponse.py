# Last updated: 12/6/2025, 5:35:00 am
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        cnts = defaultdict(int)

        ret = responses[0][0]
        for res in responses:
            for s in set(res):
                cnts[s] += 1
        
        for s in cnts.keys():
            if cnts[s] > cnts[ret] or (cnts[s] == cnts[ret] and s < ret):
                ret = s

        return ret
            

            