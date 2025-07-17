# Last updated: 17/7/2025, 8:18:15 pm
class Solution:
    def numberOfWeakCharacters(self, prop: List[List[int]]) -> int:
        n = len(prop)
        prop.sort(key=lambda x: -x[0])
        # print(prop)
        maxi = 0
        ret = 0
        i = 0

        while i < n:
            if maxi > prop[i][1]: ret += 1

            j = i + 1
            while j < n and prop[j][0] == prop[j-1][0]:
                if maxi > prop[j][1]: ret += 1
                j += 1
            
            while i < j:
                maxi = max(maxi, prop[i][1])
                i += 1
        
        return ret
            