# Last updated: 18/5/2025, 12:55:59 pm
mod = 10**9 + 7

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        colors = [0, 1, 2]
        graph = defaultdict(int)

        def generatePaths(comb, index):
            if index == m:
                graph[comb] = 1
                return
            
            prev = comb % 3
            for color in colors:
                if index > 0 and color == prev: continue
                generatePaths(comb * 3 + color, index+1)
        
        @cache
        def possiblePaths(comb, index, st):
            if index == 0:
                return [st]
            ans = []
            prev = comb % 3
            for color in colors:
                if color == prev or (color == st % 3 and index < m): continue
                ans += possiblePaths(comb // 3, index-1, st * 3 + color)
            return ans

        generatePaths(0, 0)
        fromTo = {}
        for path in graph:
            fromTo[path] = possiblePaths(path, m, 0)

        curr = graph
        for i in range(1, n):
            new_graph = defaultdict(int)
            for from_path in curr:
                for to_path in fromTo[from_path]:
                    new_graph[to_path] += curr[from_path]
                    new_graph[to_path] %= mod
            curr = new_graph
        
        ret = 0
        for path in curr:
            ret += curr[path]
            ret %= mod

        return ret