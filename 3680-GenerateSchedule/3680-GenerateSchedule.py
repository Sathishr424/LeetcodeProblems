# Last updated: 14/9/2025, 7:17:39 pm
class Solution:
    def generateSchedule(self, n: int) -> List[List[int]]:
        if n <= 3: return []
        schedule = []

        graph = [[j for j in range(n) if j != i] for i in range(n)]
        tot = n * (n - 1)
        visited = [[0] * n for _ in range(n)]

        def dfs(home, prev, retry):
            if len(schedule) == tot: return True
            if retry == n: return False
            home %= n
            if home in prev: return dfs(home + 1, prev, retry + 1)
            change = False
            for away in graph[home]:
                if away in prev or visited[home][away]: continue
                schedule.append([home, away])
                visited[home][away] = 1
                if dfs(away + 1, schedule[-1], 1): return True
                schedule.pop()
                visited[home][away] = 0
                change = True
            
            if not change: return dfs(home + 1, prev, retry + 1)
            return False
        
        dfs(0, [-1], 1)
        return schedule