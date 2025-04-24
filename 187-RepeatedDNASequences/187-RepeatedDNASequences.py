# Last updated: 24/4/2025, 5:37:53 pm
k = 10
link = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

base = 5
cache_a = {}
for i in range(1, 5):
    cache_a[i] = i * pow(base, 9)

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= k: return []

        def rolling_hash_add(num, val):
            return (num * base) + val
        
        def rolling_hash_delete(num, val):
            return num - cache_a[val]
        
        num = 0
        visited = defaultdict(int)

        for i in range(k):
            num = rolling_hash_add(num, link[s[i]])
        
        substrings = {}
        visited[num] += 1
        substrings[num] = s[:10]

        for i in range(k, n):
            num = rolling_hash_delete(num, link[s[i-k]])
            num = rolling_hash_add(num, link[s[i]])
            visited[num] += 1
            if visited[num] == 1:
                substrings[num] = s[i-k+1:i+1]

        ret = []
        for num in visited:
            if visited[num] > 1:
                ret.append(substrings[num])
        
        return ret