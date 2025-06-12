# Last updated: 12/6/2025, 5:40:24 am
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ret = 0
        for word in words:
            cons = True
            for w in word:
                if w not in allowed:
                    cons = False
                    break
            if cons: ret +=1
        return ret
            