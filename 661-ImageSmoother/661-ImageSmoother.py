# Last updated: 12/6/2025, 5:47:49 am
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])

        ret = [[0] * n for _ in range(m)]
        DIR = [-1, 0, -1, -1, 1, 0, 1, 1, -1]
        # TOP, LEFT, TOP-LEFT, TOP-RIGHT, BOTTOM, RIGHT, BOTTOM-RIGHT, BOTTOM-LEFT

        def get(i, j, total, cnt):
            if 0 <= i < m and 0 <= j < n: return [img[i][j]+total, 1+cnt]
            return [total, cnt]

        for i in range(m):
            for j in range(n):
                total, cnt = 0, 0
                for k in range(len(DIR)-1):
                    total, cnt = get(i+DIR[k], j+DIR[k+1], total, cnt)
                ret[i][j] = (total+img[i][j]) // (cnt+1)
        
        return ret