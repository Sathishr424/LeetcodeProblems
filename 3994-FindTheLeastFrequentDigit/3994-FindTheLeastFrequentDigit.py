# Last updated: 12/25/2025, 7:09:26 PM
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = defaultdict(int)
        ans = n % 10
        while n:
            freq[n % 10] += 1
            n //= 10
        
        for num in freq:
            if freq[num] < freq[ans] or (freq[num] == freq[ans] and num < ans):
                ans = num

        return ans
        