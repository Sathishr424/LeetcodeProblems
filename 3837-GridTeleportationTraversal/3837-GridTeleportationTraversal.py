# Last updated: 12/6/2025, 5:33:42 am
DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        matrix = [[a for a in matrix[i]] for i in range(m)]

        letters = [[] for _ in range(26)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] != '.' and matrix[i][j] != '#':
                    l = ord(matrix[i][j]) - 65
                    letters[l].append((i, j))
        
        stack = deque([])
        if matrix[0][0] != '.':
            for i2, j2 in letters[ord(matrix[0][0]) - 65]:
                matrix[i2][j2] = '#'
                stack.append((i2, j2, 0))
        else:
            stack.append((0, 0, 0))
            matrix[0][0] = '#'

        while stack:
            i, j, move = stack.popleft()
            if i == m-1 and j == n-1: return move

            for i2, j2 in DIR:
                i2 += i
                j2 += j

                if 0 <= i2 < m and 0 <= j2 < n and matrix[i2][j2] != '#':
                    cell = matrix[i2][j2]
                    matrix[i2][j2] = '#'
                    if cell == '.':
                        stack.append((i2, j2, move+1))
                    else:
                        for i2, j2 in letters[ord(cell) - 65]:
                            matrix[i2][j2] = '#'
                            stack.append((i2, j2, move+1))
        return -1


