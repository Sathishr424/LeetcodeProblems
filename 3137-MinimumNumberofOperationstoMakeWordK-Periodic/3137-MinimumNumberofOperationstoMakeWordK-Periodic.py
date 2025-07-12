# Last updated: 12/7/2025, 10:22:12 pm
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        n = len(word)
        cnt = defaultdict(int)
        max_word = word[:k]
        for i in range(0, n, k):
            curr = word[i:i + k]
            cnt[curr] += 1
            if cnt[curr] > cnt[max_word]:
                max_word = curr
        
        return (n // k) - cnt[max_word]


        
        