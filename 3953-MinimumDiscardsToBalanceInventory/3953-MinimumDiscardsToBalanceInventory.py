# Last updated: 12/25/2025, 7:10:21 PM
class Solution:
    def minArrivalsToDiscard(self, a: List[int], w: int, m: int) -> int:
        n = len(a)

        freq = defaultdict(int)
        window = 0
        discarded = 0
        deleted = {}
        for i in range(n):
            if window == w:
                if i-w not in deleted:
                    freq[a[i-w]] -= 1
            else:
                window += 1
            
            if freq[a[i]] + 1 > m:
                deleted[i] = 1
                # print(i, a[i], a[max(0, i - w + 1):i + 1], dict(freq))
                discarded += 1
                continue
            
            freq[a[i]] += 1

            # print(i, dict(freq), window)
            
        return discarded
        
        