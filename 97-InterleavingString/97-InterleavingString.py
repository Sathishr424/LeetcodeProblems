# Last updated: 12/6/2025, 5:53:22 am
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        l = len(s3)
        memo = {}
        def rec(i, j, index):
            if index == l: return i == m and j == n
            if i == m: return s2[j:] == s3[index:]
            if j == n: return s1[i:] == s3[index:]
            if (i, j) in memo: return False
            memo[(i,j)] = False
            if s1[i] == s3[index]:
                if rec(i+1, j, index+1): return True
            if s2[j] == s3[index]:
                if rec(i, j+1, index+1): return True
            return False
        return rec(0, 0, 0)
