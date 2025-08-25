# Last updated: 25/8/2025, 10:41:50 pm
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2: return []

        tot = finalSum // 2

        ret = []
        curr = 0
        for i in range(1, tot + 1):
            if curr + i <= tot and tot - (curr + i) > i:
                ret.append(i * 2)
                curr += i
            else:
                break
        
        if curr == tot: return ret
        ret.append((tot - curr) * 2)
        return ret