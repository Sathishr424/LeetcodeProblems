# Last updated: 12/6/2025, 5:47:03 am
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        alp = [0] * 26

        for i in range(n):
            alp[ord(s[i]) - 97] = i
        
        prev = 0
        curr = 0
        ret = []

        for i in range(n):
            if i == curr+1:
                ret.append(i-prev)
                prev = i
            curr = max(curr, alp[ord(s[i]) - 97])
        
        ret.append(n-prev)
        return ret

