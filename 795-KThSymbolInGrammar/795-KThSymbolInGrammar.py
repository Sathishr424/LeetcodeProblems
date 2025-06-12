# Last updated: 12/6/2025, 5:46:44 am
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        count = bin(k - 1).count('1')
        return 0 if count % 2 == 0 else 1