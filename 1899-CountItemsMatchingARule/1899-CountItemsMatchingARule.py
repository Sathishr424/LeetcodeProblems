# Last updated: 12/6/2025, 5:39:54 am
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ret = 0
        for i in range(len(items)):
            if ruleKey == 'type':
                if items[i][0] == ruleValue:
                    ret += 1
            elif ruleKey == 'color':
                if items[i][1] == ruleValue:
                    ret += 1
            elif ruleKey == 'name':
                if items[i][2] == ruleValue:
                    ret += 1
        return ret