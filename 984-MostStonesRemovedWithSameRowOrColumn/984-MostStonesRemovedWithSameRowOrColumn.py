# Last updated: 12/6/2025, 5:44:58 am
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)
        for s in stones:
            rows[s[0]].append(s[1])
            cols[s[1]].append(s[0])

        def dfs(row):
            visited[row] = 1
            for col in rows[row]:
                for r in cols[col]:
                    if r not in visited: dfs(r)
        cnt = 0
        visited = {}
        for row in rows:
            if row not in visited:
                cnt += 1
                dfs(row)

        return len(stones) - cnt
