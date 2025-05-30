# Last updated: 30/5/2025, 1:37:00 pm
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        candidates = {}
        ret = [-1, -1]

        def dfs(node, vis, depth):
            nonlocal ret
            if node in candidates:
                new_depth = max(depth, candidates[node])
                if ret[0] == -1 or new_depth < ret[1]:
                    ret = [node, new_depth]
                elif new_depth == ret[1]:
                    ret[0] = min(node, ret[0])
                    
                candidates[node] = max(depth, candidates[node])
            else:
                candidates[node] = depth
            
            if edges[node] != -1 and edges[node] not in vis:
                vis[edges[node]] = 1
                dfs(edges[node], vis, depth+1)
        
        dfs(node1, {node1: 1}, 0)
        dfs(node2, {node2: 1}, 0)

        return ret[0]