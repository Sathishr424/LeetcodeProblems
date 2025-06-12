# Last updated: 12/6/2025, 5:44:21 am
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)

        parents = [i for i in range(26)]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            node1 = find(x)
            node2 = find(y)

            if node1 == node2: return True

            if node1 <= node2:
                parents[node2] = node1
            else:
                parents[node1] = node2

            return False
        
        for i in range(n):
            union(ord(s1[i]) - 97, ord(s2[i]) - 97)
        
        ret = ''
        for char in baseStr:
            ret += chr(find(ord(char) - 97) + 97)
        
        return ret