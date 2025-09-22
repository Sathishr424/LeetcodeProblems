# Last updated: 23/9/2025, 12:18:52 am
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        row_graph = defaultdict(list)

        for x, y in rowConditions:
            row_graph[y].append(x)

        col_graph = defaultdict(list)

        for x, y in colConditions:
            col_graph[y].append(x)
        
        def doDfs(graph):
            arr = []
            vis = {}
            stack = {}
            
            def dfs(x, tmp_vis):
                for y in graph[x]:
                    if y in tmp_vis: return False
                    elif y not in vis:
                        tmp_vis[y] = 1
                        if not dfs(y, tmp_vis): return False
                        del tmp_vis[y]
                
                vis[x] = 1
                arr.append(x)
                return True
            
            for i in range(1, k+1): 
                if i in vis: continue
                elif not dfs(i, {}): return -1
            
            return arr

        # print(dict(col_graph))
        # print(dict(row_graph))

        row_arr = doDfs(row_graph)
        if row_arr == -1: return []
        col_arr = doDfs(col_graph)
        if col_arr == -1: return []
        
        # print(row_arr)
        # print(col_arr)

        ret = [[0 for _ in range(k)] for _ in range(k)]

        col_hash = {}

        for i, x in enumerate(col_arr):
            col_hash[x] = i

        for i in range(len(row_arr)):
            if row_arr[i] in col_hash:
                ret[i][col_hash[row_arr[i]]] = row_arr[i]
            else:
                ret[i][0] = row_arr[i]
        
        return ret
        