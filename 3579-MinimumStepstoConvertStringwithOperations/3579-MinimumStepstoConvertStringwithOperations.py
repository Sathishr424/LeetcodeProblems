# Last updated: 10/6/2025, 10:18:21 pm
class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        inf = float('inf')

        def calcCost(str1, str2, reverse):
            revCost = inf
            if not reverse:
                revCost = calcCost(str1[::-1], str2, True) + 1
            
            cost = 0
            relation = defaultdict(lambda : defaultdict(deque))
            m = len(str1)
            for i in range(m):
                a = str1[i]
                b = str2[i]

                if a != b:
                    relation[a][b].append(i)

            for i in range(m):
                a = str1[i]
                b = str2[i]
                
                if a != b:
                    if relation[b][a]:
                        index = relation[b][a].popleft()
                        str1[index], str1[i] = str1[i], str1[index]
                    cost += 1
                    relation[a][b].popleft()
            
            return min(revCost, cost)

        @cache
        def dfs(start, end):
            if start == n: return 0
            elif end >= n: return inf
            cost = dfs(start, end+1)
            
            return min(cost, calcCost(list(word1[start:end+1]), word2[start:end+1], False) + dfs(end+1, end+1))

        ans = dfs(0, 0)
        dfs.cache_clear()
        return ans