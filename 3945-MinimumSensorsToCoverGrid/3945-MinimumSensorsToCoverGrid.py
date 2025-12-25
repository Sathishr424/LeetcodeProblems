# Last updated: 12/25/2025, 7:10:29 PM
class Solution:
    def minSensors(self, m: int, n: int, k: int) -> int:
        ret = 0
        i = min(m-1, k)
        add = k * 2 + 1
        while i < m:
            j = min(n-1, k)
            curr = 0
            while j < n:
                curr += 1
                ret += 1
                if j + add >= n and j + k < n-1: 
                    ret += 1
                    curr += 1
                j += add
            if i + add >= m and i + k < m-1: 
                ret += curr
            i += add
            
        return ret