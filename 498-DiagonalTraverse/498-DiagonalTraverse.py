# Last updated: 12/6/2025, 5:48:54 am
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        ans = [[] for _ in range(m+n-1)]
        
        for i in range(m):
            for j in range(n):
                ans[i+j].append(mat[i][j])

        ret = []
        for i in range(len(ans)):
            if i % 2 == 0:
                for j in range(len(ans[i])-1, -1, -1):
                    ret.append(ans[i][j])
            else:
                for j in range(len(ans[i])):
                    ret.append(ans[i][j])
        
        return ret