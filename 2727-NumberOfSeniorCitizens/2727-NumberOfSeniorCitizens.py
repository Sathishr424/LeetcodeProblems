# Last updated: 12/6/2025, 5:37:04 am
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ret = 0
        for i in range(len(details)):
            ret += int(details[i][11]) * 10 + int(details[i][12]) > 60
        return ret