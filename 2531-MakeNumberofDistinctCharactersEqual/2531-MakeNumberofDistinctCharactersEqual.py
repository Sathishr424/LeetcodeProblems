# Last updated: 22/4/2025, 1:11:15 am
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        a = Counter(word1)
        b = Counter(word2)
        difference = len(b) - len(a)
        if abs(difference) > 2:
            return False
        for aChoice in a:
            outerDifference = difference
            if a[aChoice] == 1:
                outerDifference += 1
            for bChoice in b:
                innerDifference = outerDifference
                if aChoice == bChoice:
                    innerDifference = difference
                else:
                    if aChoice not in b:
                        innerDifference += 1
                    if bChoice not in a:
                        innerDifference -= 1
                    if b[bChoice] == 1:
                        innerDifference -= 1
                if innerDifference == 0:
                    return True
        return False