# Last updated: 12/6/2025, 5:55:38 am
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for _ in range(numRows)]
        n = len(s)

        row = 0
        col = 0
        reverse = False

        for i in range(n):
            rows[row].append(s[i])
            if (row+(not reverse)) % numRows == 0:
                if reverse:
                    reverse = False
                    row += 1
                else:
                    col += 1
                    reverse = True
                    row -= 1
            elif reverse:
                col += 1
                row -= 1
            else:
                row += 1
        
        ret = ''
        for row in rows:
            for col in row:
                ret += col
        
        return ret