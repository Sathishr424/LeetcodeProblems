# Last updated: 23/9/2025, 1:04:12 pm
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        n = max(len(version1), len(version2))

        def getVal(v):
            new_v = 0
            j = 0
            while j < len(v) and v[j] == '0':
                j += 1
            while j < len(v):
                new_v = new_v * 10 + int(v[j])
                j += 1
            return new_v

        for i in range(n):
            if i >= len(version1):
                v1 = '0'
            else:
                v1 = version1[i]
            if i >= len(version2):
                v2 = '0'
            else:
                v2 = version2[i]

            v1 = getVal(v1)
            v2 = getVal(v2)

            if v1 < v2: return -1
            elif v1 > v2: return 1
        
        return 0