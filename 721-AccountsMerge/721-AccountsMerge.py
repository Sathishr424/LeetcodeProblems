# Last updated: 12/6/2025, 5:47:25 am
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parents = [i for i in range(n)]
        sizes = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return True

            if sizes[node2] > sizes[node1]:
                node1, node2 = node2, node1
            
            sizes[node1] += sizes[node2]
            parents[node2] = node1

            return False

        emails = {}

        for i in range(n):
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                if email in emails:
                    union(i, emails[email])
                
                emails[email] = i

        ret = defaultdict(list)

        for email in emails:
            ret[find(emails[email])].append(email)
        
        res = []
        for i in ret:
            res.append([accounts[i][0]] + sorted(ret[i]))

        return res