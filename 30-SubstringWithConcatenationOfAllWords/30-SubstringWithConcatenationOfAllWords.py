# Last updated: 12/6/2025, 5:54:48 am
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counts = defaultdict(int)
        k = len(words[0])

        for word in words:
            counts[word] += 1
        
        n = len(s)
        tot = len(counts)

        res = []
        vis = {}
        for i in range((n-(n%k))-k+1):
            if i in vis: continue
            vis[i] = 1

            curr = s[i:i+k]
            if curr not in counts: continue

            there = defaultdict(int)
            matches = 0
            j = i
            left = i

            while j+k <= n:
                curr = s[j:j+k]
                if curr in counts:
                    there[curr] += 1
                    if there[curr] == counts[curr]:
                        matches += 1
                    elif there[curr] > counts[curr]:
                        while j > left:
                            j -= k
                            del vis[j]
                        break
                    if matches == tot:
                        res.append(left)
                        matches -= 1
                        tmp = s[left:left+k]
                        there[tmp] -= 1
                        left += k
                    vis[j] = 1
                else: break
                j += k

        return res