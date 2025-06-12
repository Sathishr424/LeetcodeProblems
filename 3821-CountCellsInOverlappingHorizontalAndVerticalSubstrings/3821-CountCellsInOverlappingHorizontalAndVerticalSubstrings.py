# Last updated: 12/6/2025, 5:33:53 am
class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        # grid = [[0] * 1000 for _ in range(1000)]
        m = len(grid)
        n = len(grid[0])
        tot = m*n

        """
        [["v","s","d","s"],
         ["i","d","s","t"],
         ["d","s","s","k"]]

         ds

         [["a","b","a"],
          ["b","a","b"],
          ["a","b","a"]]

        "ababababa"
        """

        k = len(pattern)
        lps = [0] * k

        i = 1
        j = 0
        while i < k:
            if pattern[i] == pattern[j]:
                j += 1
                lps[i] = j
            elif j > 0:
                j = lps[j-1]
                continue
            i += 1

        h_cells = []
        v_cells = []

        l = 0
        for i in range(m):
            j = 0
            while j < n:
                pos = i * n + j
                
                if grid[i][j] == pattern[l]:
                    if l+1 == k:
                        h_cells.append(pos)
                        if l > 0:
                            l = lps[l-1]
                            continue
                    else:
                        l += 1
                elif l > 0:
                    l = lps[l-1]
                    continue
                j += 1
        l = 0
        for j in range(n):
            i = 0
            while i < m:
                pos = j * m + i
                
                if grid[i][j] == pattern[l]:
                    if l+1 == k:
                        v_cells.append(pos)
                        if l > 0:
                            l = lps[l-1]
                            continue
                    else: l += 1
                elif l > 0:
                    l = lps[l-1]
                    continue
                i += 1

        visited_h = [0] * tot
        visited_v = [0] * tot

        for val in h_cells:
            for i in range(val, val-k, -1):
                if visited_h[i] == 1: break
                visited_h[i] = 1

        for val in v_cells:
            for i in range(val, val-k, -1):
                y = i % m
                x = i // m
                pos = y * n + x
                if visited_v[pos] == 1: break
                visited_v[pos] = 1
        
        ret = 0
        for pos in range(tot):
            if visited_v[pos] == 1 and visited_h[pos] == 1: ret += 1

        return ret
            