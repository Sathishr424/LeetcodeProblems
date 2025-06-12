# Last updated: 12/6/2025, 5:37:37 am
class Solution:
    def bestClosingTime(self, cust: str) -> int:
        nextV = 0
        nextNV = 0
        for c in cust:
            if c == 'Y': nextV += 1
            elif c == 'N': nextNV += 1
        prevV = 0
        prevNV = 0
        prevType = ''
        ret = [float('inf'), -1]
        for i,c in enumerate(cust):
            if not prevType:
                if nextV < ret[0]: ret = [nextV, i]
                if c == 'Y': nextV -= 1
                else: nextNV -= 1
                prevType = c
            else:
                if prevType == 'Y': prevV += 1
                else: prevNV += 1
                if nextV + prevNV < ret[0]: ret = [nextV + prevNV, i]
                if c == 'Y': nextV -= 1
                else: nextNV -= 1
                prevType = c
        tmp = prevNV+(prevType == 'N')
        if tmp < ret[0]:
            ret = [tmp, len(cust)]
        return ret[1]

