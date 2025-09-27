# Last updated: 28/9/2025, 2:22:56 am
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        if k == 0: return True
        n = len(s)

        indexes = defaultdict(list)

        for i in range(n):
            indexes[s[i]].append(i)

        used = [0] * n
        for char in sorted(indexes.keys(), key=lambda x: indexes[x][-1] - indexes[x][0]):
            l = indexes[char][0]
            r = indexes[char][-1]

            i = l + 1
            while i < r:
                if indexes[s[i]][0] < l or used[indexes[s[i]][-1]]: break
                r = max(r, indexes[s[i]][-1])
                i += 1
            else:
                if r - l + 1 != n:
                    for i in range(l, r+1):
                        used[i] = 1
                    k -= 1
                    if k == 0: return True
        
        return False
