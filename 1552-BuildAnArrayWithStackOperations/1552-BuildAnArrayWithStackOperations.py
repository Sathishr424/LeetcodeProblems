# Last updated: 12/6/2025, 5:41:39 am
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        prev = 0
        ret = []
        i = 1
        index = 0
        while prev != target[-1]:
            if prev:
                if prev != target[index]:
                    ret.append('Pop')
                    prev = prev-1
                else: 
                    index += 1
            prev = i
            ret.append('Push')
            i += 1
        return ret
                