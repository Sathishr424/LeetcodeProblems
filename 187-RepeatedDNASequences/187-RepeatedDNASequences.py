# Last updated: 24/4/2025, 4:04:03 pm
k = 10
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= k: return []
        base = 5
        mod = 10**9 + 7

        link = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

        cache = pow(base, 9, mod)

        def rolling_hash_add(num, val):
            return ((num * base % mod) + val) % mod
        
        def rolling_hash_delete(num, val):
            return (num - (val * cache % mod)) % mod
        
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