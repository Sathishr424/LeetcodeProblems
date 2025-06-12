# Last updated: 12/6/2025, 5:37:39 am
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(dict)
        n = len(amount)

        for x, y in edges:
            graph[x][y] = 1
            graph[y][x] = 1

        res = 0

        def dfs(node, vis, index):
            if node == 0: return True
            elif node in vis: return False

            vis[node] = index
            
            for y in graph[node]:
                if y not in vis and dfs(y, vis, index+1): return True
            
            del vis[node]

            return False
        
        def dfs_alice(node, vis, index):
            ans = 0

            if node not in bob_visited:
                ans += amount[node]
            else:
                if bob_visited[node] == index:
                    ans += amount[node] / 2
                elif index < bob_visited[node]:
                    ans += amount[node]
            
            if len(graph[node]) == 0: return ans

            curr = -float('inf')
            for y in list(graph[node].keys()):
                del graph[node][y]
                del graph[y][node]
                curr = max(curr, dfs_alice(y, vis, index+1))

            return curr+ans
        
        bob_visited = {}
        dfs(bob, bob_visited, 0)
        return int(dfs_alice(0, {0: 1}, 0))