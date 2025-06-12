# Last updated: 12/6/2025, 5:42:11 am
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ret = []
        for i in range(m):
            ret.append([0, i])
            for j in range(n):
                ret[-1][0] += mat[i][j]
        ret.sort(key=lambda x: x[0])
        ans = []
        for i in range(k):
            ans.append(ret[i][1])
        return ans
