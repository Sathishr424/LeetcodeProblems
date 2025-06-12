# Last updated: 12/6/2025, 5:36:29 am
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        # if len(s2) > len(s1):
        #     s1, s2 = s2, s1
        
        m = len(s1)
        n = len(s2)

        odd = defaultdict(int)
        even = defaultdict(int)

        for i in range(m):
            if i % 2 == 0:
                even[s1[i]] += 1
            else:
                odd[s1[i]] += 1
        
        for i in range(n):
            if i % 2 == 0:
                if s2[i] not in even: return False
                even[s2[i]] -= 1
                if even[s2[i]] == 0: del even[s2[i]]
            else:
                if s2[i] not in odd: return False
                odd[s2[i]] -= 1
                if odd[s2[i]] == 0: del odd[s2[i]]
                

        return len(odd) == 0 and len(even) == 0