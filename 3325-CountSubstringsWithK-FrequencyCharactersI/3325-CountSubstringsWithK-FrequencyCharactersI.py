# Last updated: 25/7/2025, 8:11:10 pm
class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ret = 0

        maxi = [[] for _ in range(26)]
        prefix = [[0] * 26 for _ in range(n)]
        
        for i in range(n):
            prefix[i][ord(s[i]) - ord('a')] += 1
            for j in range(26):
                prefix[i][j] += prefix[i - 1][j]
                maxi[j].append(prefix[i][j])

        for i in range(n-k+1):
            smallest = n
            curr = ord(s[i]) - ord('a')
            for a in range(26):
                need = prefix[i][a] + k
                if a == curr:
                    need -= 1
                index = bisect_left(maxi[a], need, lo=i + k - 1)
                # print(i, (curr, a), chr(a + ord('a')), need, index)

                smallest = min(index, smallest)
            ret += n - smallest

        return ret